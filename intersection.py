list1=[1,2,3,4,5,6,7]
list2 = [2,3,4,9]

print(list1)
print(list2)

list3 = list(filter(lambda x: x in list1, list2))
print(list3)