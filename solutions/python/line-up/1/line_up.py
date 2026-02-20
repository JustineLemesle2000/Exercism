def line_up(name, number):
    str_number = str(number)
    if not str_number.endswith('11') and str_number.endswith('1'): 
        str_number += "st"
    elif not str_number.endswith('12') and str_number.endswith('2'):
        str_number += "nd"
    elif not str_number.endswith('13') and str_number.endswith('3'):
        str_number += "rd"
    else :
        str_number += "th"

    return f"{name}, you are the {str_number} customer we serve today. Thank you!" 