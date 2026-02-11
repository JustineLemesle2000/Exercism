def score(x, y):
    distance = pow(x*x + y*y, 0.5)
    score = [10, 5, 1]
    anneaux = [1, 5, 10]
    for nb in range(len(anneaux)) :
        if distance <= anneaux[nb] :
            return score[nb]
    return 0
