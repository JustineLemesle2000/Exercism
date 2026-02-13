def color_code(color):
    for index, item in enumerate(colors()) : 
        if item == color :
            return index 
def colors():
    return ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
