def is_armstrong_number(number):
    carac = str(number)
    taille = len(carac)
    result = 0 
    for nb in carac :
        result += int(nb) ** taille
    return result == number
        
