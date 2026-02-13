def label(colors):
    color = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']
    resnum = 0
    res = ''
    count = 0
    rep = ''
    for index, couleur in enumerate(color) : 
        if colors[0] == couleur :
            resnum += index * 10
        if colors[1] == couleur :
            resnum += index
        if colors[2] == couleur :
            nbZero = index
    res = resnum * (10 ** nbZero)

    while res > 1000 :
        res = res // 1000
        count += 1 
        
    res = str(res)
    if count == 0 :
        rep = res + ' ohms'
    elif count == 1 :
        rep = res + ' kiloohms'
    elif count == 2  :
        rep = res + ' megaohms'
    else :
        rep = res + ' gigaohms'
    return rep 
        
    