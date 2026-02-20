def flatten(iterable):
    res = []
    for element in iterable :
        if isinstance(element, list) :
            res.extend(flatten(element))
        elif element != None :
            res.append(element)
    return res 
            
    
