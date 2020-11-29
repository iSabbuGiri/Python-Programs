person = [{'name':'ram', 'age':60}, {'name':'hari', 'age':50}]
print("Old data:")
print(person)
new_list = sorted(person, key = lambda x: x['age'])
print("New List:")
print(new_list)