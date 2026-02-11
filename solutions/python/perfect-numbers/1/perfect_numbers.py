def classify(number):
    if number < 1 :
        raise ValueError("Classification is only possible for positive integers.")
    aliquote = set()
    autre = 0
    for nb in range(1, int(number**0.5) + 1):
        if number % nb == 0:
            if nb != number:
                aliquote.add(nb)
            autre = number // nb
            if autre != number and autre != nb : 
                aliquote.add(autre)
    somme = sum(aliquote)
    if number == somme :
        return "perfect"
    elif number < somme :
        return "abundant"
    else :
        return "deficient"

