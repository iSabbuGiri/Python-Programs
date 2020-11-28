string = input("Enter the list of words:")

x = string.split()
largest = len(x[0])

for i in x:
    if len(i) > largest:
        largest = len(i)
print("Largest length is:",largest)


