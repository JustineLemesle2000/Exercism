'''Fonction pour déconstruire des listes imbriqués '''
def flatten(iterable):
    res = []
    for element in iterable :
        if isinstance(element, list) :
            res.extend(flatten(element))
        elif element is not None :
            res.append(element)
    return res 
            
    
