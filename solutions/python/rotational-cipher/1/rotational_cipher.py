def rotate(text, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for lettre in text: 
        if lettre.isalpha() : 
            if lettre.isupper():
                index = alphabet_maj.find(lettre)
                newindex = (index + key) % 26
                newlettre = alphabet_maj[newindex]
                result += newlettre
            else : 
                index = alphabet.find(lettre)
                newindex = (index + key) % 26
                newlettre = alphabet[newindex]
                result += newlettre
        else : 
            result += lettre
    return result