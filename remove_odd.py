def odd_value(str):
    s1 = ""
    for i in range(len(str)):
        if i%2 == 0:
            s1+= str[i]
    return s1    
print(odd_value("python"))        
