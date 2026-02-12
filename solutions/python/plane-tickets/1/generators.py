"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    letters = ["A","B","C","D"]
    index = 0
    while number: 
        yield letters[index]
        index = (index + 1) % len(letters)
        number -= 1 


def generate_seats(number):
    row = 1
    letters = generate_seat_letters(number)
    for index in range(number):
        if row == 13 :
            row += 1
        letter = next(letters)
        yield  str(row) + str(letter) 
        number -= 1   
        if (index + 1) % 4 == 0:
            row +=1 

def assign_seats(passengers):
    result = dict()
    seats = generate_seats(len(passengers))

    for passenger in passengers :
        seat = next(seats)
        result[passenger] = seat
    return result 

def generate_codes(seat_numbers, flight_id):
    result = ''
    for ticket in seat_numbers : 
        result = ticket + flight_id
        while len(result) < 12 : 
            result += '0'
        yield result
                
