class InvaliedSeatNumberError(Exception):
    pass

def SeatNumber(movie_name,seat):
    if seat<0:
        raise InvaliedSeatNumberError("Seat number Cant be negetive...")
    else:
        print("Ticket Booked.....")

try:
    SeatNumber("Toxic",1)
except InvaliedSeatNumberError as e:
    print(e)