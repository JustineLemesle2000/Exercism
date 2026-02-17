def resistor_label(colors):
    color_tolerance = {'grey' : '0.05', 'violet' : '0.1', 'blue' : '0.25', 'green' : '0.5', 'brown' : '1', 'red' : '2', 'gold' : '5', 'silver' : '10'}
    
    color = {'black': 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4, 'green' : 5, 'blue' : 6, 'violet' : 7, 'grey' : 8, 'white' : 9}
    if len(colors) == 1 :
        return '0 ohms'     
    if len(colors) == 4 : 
        value = color[colors[0]] * 10 + color[colors[1]]
        multiplicateur = 10 ** color[colors[2]]
    else :  
        value = color[colors[0]] * 100 + color[colors[1]] * 10 + color[colors[2]]
        multiplicateur = 10 ** color[colors[3]]

    resistance = value * multiplicateur

    if resistance >= 1000000:
        unit = " megaohms"
        resistance /= 1000000
    elif resistance >= 1000:
        unit = " kiloohms"
        resistance /= 1000
    else :
        unit = " ohms"

    tolerance = color_tolerance[colors[-1]]
    if resistance % 1 == 0:
        resistance = str(int(resistance))
    else : 
        resistance = str(resistance)
    return resistance + unit + ' ±' + tolerance + '%'