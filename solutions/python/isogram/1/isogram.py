def is_isogram(string):
    string = string.lower()
    texte = set()
    
    for lettre in string : 
        if lettre.isalpha():
            if lettre in texte :
                return False
            texte.add(lettre)
    return True
        

    
    