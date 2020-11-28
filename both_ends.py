def both_ends(str):
    if len(str) < 2:
        return ''
    else:
        return str[:2] + str[-2:]    
     
print (both_ends("Python"))