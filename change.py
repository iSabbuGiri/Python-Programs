def specialreplace(str):
    return str[0] + str.replace(str[0], '$')[1:]
print(specialreplace('restart'))    