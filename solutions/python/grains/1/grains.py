def square(number):
    if( 0 < number < 65 ) : 
        return 2 ** (number-1)
    raise ValueError("square must be between 1 and 64")
    
def total():
    res = 0
    for nb in range(64) : 
        res += 2 ** nb
    return res
        
