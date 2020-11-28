lst = [{}, {}, {}]
another_list = [{1,2}, {}, {}]

print(all(not i for i in lst))
print(all(not i for i in another_list))