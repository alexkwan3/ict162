from guest import *
from amenity import *
from datetime import *
from booking import *

class Hotel:
    '''models a hotel
    it has 5 attributes: _name (str), _guests (dict), _amenities (list), _bookings (dict), _roomAvailability (dict)
    it has mutator methods: setUpGuests(), setUpAmenities(), setUpRoomAvailability(), saveRoomAvailability(), submitBooking(), cancelBooking(), checkIn()
    it has accessor methods: searchGuest(), checkRoomAvailability(), listAmenity(), getAmenity(), searchBooking(), searchBookingByPassport()'''
    
    def __init__(self, name, roomFilename):
        self._name = name
        self._guests = self.setupGuests()
        self._amenities = self.setupAmenities()
        self._roomAvailability = self.setupRoomAvailability(roomFilename) 
        self._bookings = {}
    
    def setupGuests(self):
        guests = {}
        infile = open("Guests.txt", "r") 
        for line in infile:
            pp,name,country = line.split(",")
            guests[pp.strip()] = Guest(pp.strip(),name.strip(),country.strip()) 
        infile.close()
    
        infile = open("Blacklist.txt", "r")
        for line in infile:
            pp, dateReported, reason = line.split(",") 
            g = guests.get(pp.strip())
            if g is not None:
                g.blacklist(datetime.strptime(dateReported.strip(), "%d-%b-%Y").date(), reason.strip())
        infile.close()
        return guests
    
    def setupAmenities(self):
        amenities = []
        infile = open("SharedAmenity.txt", "r") 
        for line in infile:
            itemCode,desc,price = line.split(",")
            amenities.append( SharedAmenity(itemCode, desc, float(price))) 
        infile.close()
        
        infile = open("InRoomAmenity.txt", "r") 
        for line in infile:
            itemCode,desc,price,floorArea = line.split(",")
            amenities.append( InRoomAmenity(itemCode, desc, float(price), float(floorArea)))
        infile.close()
        return amenities
    
    def setupRoomAvailability(self, filename): 
        roomAvailability = {}
        infile = open(filename, "r")
        for line in infile:
            dateString, standardCount, deluxeCount = line.split(",")
            thisDate = datetime.strptime(dateString, "%d-%b-%Y").date() 
            roomAvailability[thisDate] = [int(standardCount), int(deluxeCount)]
        infile.close()
        return roomAvailability
    
    def saveRoomAvailability(self, filename): 
        outfile = open(filename, "w")
        for k, v in self._roomAvailability.items():
            print("{},{},{}".format(k.strftime("%d-%b-%Y"), v[0], v[1]), file=outfile) 
        outfile.close()
        
    def searchGuest(self, ppNo):
        if ppNo in self._guests.keys():
            return self._guests[ppNo]
        else:
            return None
    
    def checkRoomAvailability(self, type, start, end):
        self._unavailableDates = []
        if start > end:
            return False
        elif start not in self._roomAvailability or end not in self._roomAvailability:
            return False
        elif type == 'Standard' or type == 'Deluxe':
            for k, v in self._roomAvailability.items():
                if k >= start and k <= end:
                    if type == 'Standard' and v[0] == 0:
                        self._unavailableDates.append(k)
                    if type == 'Deluxe' and v[1] == 0:
                        self._unavailableDates.append(k)
            if self._unavailableDates != []:
                return False
            else:
                return True
        else:
            return False
            
    def listAmenity(self):
        txt = 'List of Amenities\n=================\n'
        for n in range (len(self._amenities)):
            txt += f'{n+1}.\t{self._amenities[n]}\n' # looks nicer with index
        return txt
    
    def getAmenity(self, code):
        for n in self._amenities:
            if n.itemCode == code:
                return n
        return None
    
    def searchBooking(self, bkID):
        if bkID in self._bookings.keys():
            return self._bookings[bkID]
        else:
            return None
        
    def searchBookingByPassport(self, ppNo):
        guestbookinglist = []
        txt = ''
        for k, v in self._bookings.items():
            if ppNo == v.passport:
                guestbookinglist.append(v)
        if guestbookinglist == []:
            return guestbookinglist # returns an empty list if no Booking object found
        else:
            for n in guestbookinglist:
                txt += f'{n}\n'
            return txt # returns all bookings made by passport number
    
    def submitBooking(self, bk):
        if bk.status != 'Pending':
            raise BookingException (f'Error! Booking status is {bk.status}!')
        elif self.checkRoomAvailability(bk.roomType, bk.checkInDate, bk.checkOutDate) is False:
            if self._unavailableDates != []:
                txt = ''
                for n in self._unavailableDates:
                    txt += f'{n:%d-%b-%Y}\n'
                raise BookingException (f'\nNo available {bk.roomType} rooms on:\n{txt}') 
                # prints out which exact dates are unavailable
            else:
                raise BookingException (f'No available {bk.roomType} rooms from {bk.checkInDate:%d-%b-%Y} to {bk.checkOutDate:%d-%b-%Y}')
                # if dates not in April / txt file provided
        else:
            # fw = open('Rooms_April2023.txt', 'w')
            fw = open('Rooms_April2023v2.txt', 'w') 
            # separate from original file to make it easier to run repeatedly
            for k, v in self._roomAvailability.items():
                if k >= bk.checkInDate and k <= bk.checkOutDate:
                    if bk.roomType == 'Standard':
                        v[0] -= 1
                    if bk.roomType == 'Deluxe':
                        v[1] -= 1
                print (f'{k:%d-%b-%Y}, {v[0]}, {v[1]}', file = fw)
            fw.close()
            bk.status = 'Confirmed'
            self._bookings[bk.bookingID] = bk
            
    def cancelBooking(self, bkID):
        if self.searchBooking(bkID) is None:
            raise BookingException (f'Error! No such booking ID: {bkID}')
        elif self._bookings[bkID].status != 'Confirmed':
            raise BookingException (f'Error! This booking ({bkID}) cannot be cancelled due to {self._bookings[bkID].status} status!')
        else:
            self._bookings[bkID].status = 'Cancelled'
            fw = open ('Rooms_April2023v2.txt', 'w')
            for k, v in self._roomAvailability.items():
                if k >= self._bookings[bkID].checkInDate and k <= self._bookings[bkID].checkOutDate:
                    if self._bookings[bkID].roomType == 'Standard':
                        v[0] += 1
                    if self._bookings[bkID].roomType == 'Deluxe':
                        v[1] += 1
                print (f'{k:%d-%b-%Y}, {v[0]}, {v[1]}', file = fw)
            fw.close()
            
    def checkIn(self, bkID, roomNum):
        if self.searchBooking(bkID) is None:
            raise BookingException (f'Error! No such booking ID ({bkID})!')
        else:
            self._bookings[bkID].checkIn(roomNum)