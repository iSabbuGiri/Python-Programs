str1 = "google.com"

dict = {}

for n in str1:
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1
print("The expected output is:" + str(dict))            