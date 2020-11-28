subject = [('maths', 80), ('physics', 65), ('chemistry', 78)]
print(subject)
subject.sort(key = lambda x : x[1])
print(subject)