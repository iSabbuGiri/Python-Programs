lst = []
num = int(input("How many numbers:"))

for i in range(num):
    numbers = int(input("Enter number:"))
    lst.append(numbers)

print("The largest number is:", max(lst))    