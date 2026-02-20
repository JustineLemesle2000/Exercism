def find(search_list, value):
    liste = sorted(search_list)
    if not liste : 
        raise ValueError("value not in array")
    original = liste.copy()
    while len(liste) > 1 : 
        middle = liste[len(liste) // 2]
        middle_index = liste.index(middle) 
        if value == middle:
            return original.index(value)
        if value > middle : 
            liste = liste[middle_index + 1:]
        elif value < middle : 
            liste = liste[:middle_index]     
        
    if liste[0] == value :
        return original.index(value)
    else :
        raise ValueError("value not in array")