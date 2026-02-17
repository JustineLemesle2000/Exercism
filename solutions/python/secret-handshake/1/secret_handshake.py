def commands(binary_str):
    secret ={"00001" : "wink","00010" : "double blink","00100" : "close your eyes", "01000" : "jump"}
    result = []
    reverse = False
    key = ""
    for bit in range(5) :
        if binary_str[4 - bit] == "1" : 
            key = "0" * (4-bit) + "1" + "0"* bit
            if key == "10000":
                reverse = True
            else : 
                result.append(secret[key])
            
    if reverse:
        result.reverse()

    return result