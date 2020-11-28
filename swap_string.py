fs = input("Enter a first string:")
ss = input("Enter a second string:")

x = fs[:2]


fs = fs.replace(fs[:2], ss[:2])
ss = ss.replace(ss[:2],x)

print(fs, ss)