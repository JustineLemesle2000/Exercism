def is_valid(isbn):
    text = isbn.replace("-", "")
    if len(text) != 10 :
        return False
    for nb in range(9):
        if not text[nb].isdigit():
            return False
    if not(text[-1].isdigit() or text[-1] == "X"):
        return False
        
    calcul = 0
    for nb in range(10) :
        poids = 10 - nb 
        if nb == 9 and text[-1] == "X" : 
            valeur = 10
        else :
            valeur = int(text[nb])
        calcul += poids * valeur
    return calcul % 11 == 0 
        
        
        
