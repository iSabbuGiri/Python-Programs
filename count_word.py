def count(str):
    dict ={}
    words = str.split()

    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict  
print(count("I am a programmer. I am a student."))            