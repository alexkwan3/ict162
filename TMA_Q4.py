from booking import *
from hotel import *

def enterBkID():
    while True:
        bkID = input ("Enter booking ID to search: ")
        if bkID.isdigit():
            break
        else:
            print ("Please enter numbers only.")
    bkID = int(bkID)
    return bkID

def q4():
    ht = Hotel('SAMI Hotel', 'Rooms_April2023.txt')
    try:
        while True:
            samihotel = ("@@@@ SAMI Hotel @@@@")
            print (samihotel)
            print ('=' * len(samihotel))
            print ('1. Submit Booking\n' +\
                '2. Cancel Booking\n' +\
                '3. Search Booking(s)\n' +\
                '4. Check-In\n' +\
                '0. Exit')
            option = input ("Enter option: ")
            if option == '0':
                print ("Program end.")
                break
            elif option == '1':
                passport = input ("Enter passport number to start: ").upper()
                if ht.searchGuest(passport) is not None:
                    print ("Guest located. Please verify\n" +\
                        f'\n{ht._guests[passport]}\n')
                    if ht._guests[passport].isBlacklisted() == True:
                        print (f'Guest ({ht._guests[passport].name}) is blacklisted.\n')
                    else:
                        while True:
                            rmtype = input ('Select preferred room type (S)tandard or (D)eluxe: ').upper()
                            if rmtype == 'S':
                                rm = 'Standard'
                                rmPrice = 16.99
                                break
                            elif rmtype == 'D':
                                rm = 'Deluxe'
                                rmPrice = 19.99
                                break
                            else:
                                print ("Invalid room type. Please choose again.")
                        while True:
                            bdtype = input ('Select preferred bed type (S)ingle or s(U)per: ').upper()
                            if bdtype == 'S':
                                bd = Bed ('Single', 10.99, 'Single bed with one pillow and one blanket')
                                break
                            elif bdtype == 'U':
                                bd = Bed ('Super', 12.99, 'Super single bed with one pillow and one blanket')
                                break
                            else:
                                print ("Invalid bed type. Please choose again.")
                        room = Room (rm, rmPrice, bd)
                        print ()
                        print (ht.listAmenity())
                        while True:
                            amenitychoice = input ("Enter item code to add or <enter> to stop: ").upper()
                            if amenitychoice == '':
                                break
                            amty = ht.getAmenity(amenitychoice)
                            if amty is not None:
                                if room.addAmenity(amty) == True:
                                    print (f'{amenitychoice} added...')
                            else:
                                print (f"Item code ({amenitychoice}) not valid. Please try again.")
                        while True:
                            CID = input ("\nEnter Check-In date in DD-MON-YYYY: ")
                            COD = input ("Enter Check-Out date in DD-MON-YYYY: ")
                            try:
                                chkInDate = datetime.strptime(CID, '%d-%b-%Y').date()
                                chkOutDate = datetime.strptime(COD, '%d-%b-%Y').date()
                                if chkInDate >= chkOutDate:
                                    print ("Check out date must be at least 1 day after check in date.")
                                else:
                                    break
                            except ValueError:
                                print ("Date format is wrong. Please try again")
                        # print (f'{chkInDate:%d-%b-%Y}, {chkOutDate:%d-%b-%Y}')
                        bk = Booking (ht._guests[passport], room, chkInDate, chkOutDate)
                        print ('\n', bk, '\n')
                        while True:
                            submitbk = input ("Proceed to submit booking? (Y/N): ").upper()
                            if submitbk == 'Y':
                                ht.submitBooking(bk)
                                print ("Booking is submitted.\n")
                                break
                            elif submitbk == 'N':
                                print ("Booking not submitted.\n")
                                break
                            else:
                                print ("Invalid option. Please enter Y or N.")
                else:
                    print ("No such guest. Please try again.\n")
            elif option == '2':
                bkID = enterBkID()
                if ht.searchBooking(bkID) is not None:
                    if ht._bookings[bkID].status == 'Cancelled':
                        print ("The booking status is 'Cancelled'. Cannot cancelled.")
                    else:
                        ht.cancelBooking(bkID)
                        print ('Booking is cancelled...')
                else:
                    print ("There is no such booking...")
            elif option == '3':
                searchid = input ("Search by booking ID or passport? (B/P): ").upper()
                if searchid == 'B':
                    bkID = enterBkID()
                    if ht.searchBooking(bkID) is not None:
                        print (ht.searchBooking(bkID), '\n')
                    else:
                        print ('No booking found.')
                elif searchid == 'P':
                    pp = input ("Enter passport number to search: ").upper()
                    if ht.searchBookingByPassport(pp) == []:
                        print ("No booking found.")
                    else:
                        print (ht.searchBookingByPassport(pp))
                else:
                    print ("Invalid option. Please try again.")
            elif option == '4':
                bkID = enterBkID()
                if ht.searchBooking(bkID) is None:
                    print ('Booking not found.')
                else:
                    print ('Please verify Guest and Room details...')
                    print (ht.searchBooking(bkID), '\n')
                    rmNum = input ("Enter allocated room number or <enter> to cancel check-in: ")
                    if rmNum == '':
                        print ("Check-in aborted.")
                    else:
                        ht.checkIn(bkID, rmNum)
                        print ("Checked-in. Enjoy your stay at SAMI.")
            else:
                print ("Invalid option. Please choose again.")
    except BookingException as e:
        print (e)
    except MinFloorAreaException as m:
        print (m)
q4()