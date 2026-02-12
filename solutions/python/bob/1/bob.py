def response(hey_bob):
    hey_bob = hey_bob.strip()
    question = hey_bob.endswith('?')
    if hey_bob == "" :
        return "Fine. Be that way!"
    cri = True
    lettre = False
    for char in hey_bob:
        if char.isalpha() :
            lettre = True
            if not char.isupper():
                cri = False
                break          
    if cri and question and lettre:
        return "Calm down, I know what I'm doing!"
    elif cri and lettre: 
        return "Whoa, chill out!"
    elif question :
        return "Sure."
    return "Whatever."
    
    