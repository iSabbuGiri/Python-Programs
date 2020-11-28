def testrange(x,y,n):
    if n in range(x,y):
        print("is in range.")
    else:
        print("outside the given range.")       
   


x = int(input("Enter the lower limit:"))
y = int(input("Enter the upper limit:"))
n = int(input("Enter a number:"))

testrange(x,y,n)

