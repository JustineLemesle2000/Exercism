def equilateral(sides):
    if not triangle(sides) : 
        return False
    return sides[0] == sides[1] and sides[1] == sides[2] and sides[2] == sides[0] 
    
def isosceles(sides):
    if not triangle(sides) : 
        return False
    return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]

def scalene(sides):
    if not triangle(sides) : 
        return False
    return sides[0] != sides[1] and sides[1] != sides[2] and sides[2] != sides[0]

def triangle(sides):
    if sides[0] + sides[1] + sides[2] > 0 :  
        if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[2] + sides[0] >= sides[1] :
            return True
    return False