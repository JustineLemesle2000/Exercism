def value(colors):
    color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    res = 0
    for index, couleur in enumerate(color) : 
        if colors[0] == couleur :
            res += index * 10
        if colors[1] == couleur :
            res += index
    return res
