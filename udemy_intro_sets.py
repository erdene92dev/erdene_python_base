# sets are unordered collection of unique items

myset = set()
myset.add("item 1")

print(myset)

myset.add(2)

print(myset)

# if you have a list of items and you want to get only unique values in the list
# you can perform set on the list

list_1 = [1,1,1,2,2,2,2,3,3,3,3,3] 

myset2 = set(list_1)
print('\nunique items within list 1 ex:')
print(myset2)