str = "The quick Brown Fox"

lowercase = 0
uppercase = 0

for s in str:

    if (s.islower()):
        lowercase += 1
    elif(s.isupper()):
        uppercase += 1

print(lowercase)
print(uppercase)        
    