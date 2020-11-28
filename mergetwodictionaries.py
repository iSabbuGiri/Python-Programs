dict1 = {1 :"one", 2:"two", 3:"three"}
dict2 = {4:"four", 5:"five"}

new_dict = {**dict1, **dict2} # merges two dictionary and gives a new value

print(new_dict)