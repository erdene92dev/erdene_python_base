# dictionaries start with key and value pair within curly brackets, for ex

from datetime import datetime

todays_date = datetime.today()

print("Today's date is :")
print(todays_date)

dict_1 = {'user_id':1005, 'product':'play duo headset', 'price':299.0}
# dictionaries can hold various data types such as strings, integers, and floats

print('\nmy first dictionary :')

print(dict_1)

print('\nuser_id values from my first dictionary dict_1 are: ')

print(dict_1['user_id'])

# dictionaries can also hold lists and other dictionaries
# its not common but it is support
dict_2 = {'k1':125, 'k2':['apple','banana','watermelon'],'k3':{'nestkey1':'nested Pie', 'nestkey2':'playduo'}}

print('\nMy second dictionary can hold lists and dictionaries!: ')
print(dict_2)

# print key 2 from dictionary 2, dict_2
k2_value = dict_2['k2']
print('\nThe k2 value in dict_2 is: ')
print(k2_value)

# print nestkey1 value
print('\nThe k3 nested key value in dict_2 is: ')
print(dict_2['k3']['nestkey1'])

# print the 3rd item from the list within dict_2
print('\nThe third item in k2 of dict_2 is: ')
print(dict_2['k2'][2])

## change the nestkey value 2 in k3 to UPPER case
print('\nnestkey value change within dict_2 ex.1: ')
k3_nk2 = dict_2['k3']['nestkey2'] 
k3_nk2 = k3_nk2.upper()
dict_2['k3']['nestkey2'] = k3_nk2
print(dict_2)

# or you can do the following, change the nestkey value 2 in k3 to Title case
print('\nnestkey value change within dict_2 ex.2: ')
dict_2['k3']['nestkey2'] = k3_nk2.title()
print(dict_2)

# change the second list index within key 2
print('\nk2 list index change within dict_2 ex.1 ')
dict_2['k2'][1] = 'kiwi'
print(dict_2)

# you can also add new keys into existing dictionaries
dict_3 = {'k1':'a','k2':'b','k3':'c','k4':'d'}
print('\nKey addition example on dict_3: ')
print('dict_3 before addition: ')
print(dict_3)

# add the letter
dict_3['k5']='e'
print('dict_3 after addition: ')
print(dict_3)

# show all keys in dict_3
print('\nShow all keys in dict_3')
print(dict_3.keys())


# show all values in dict_3
print('\nShow all values in dict_3')
print(dict_3.values())

# show all pairings in dict_3
print('\nShow all pairings in dict_3')
print(dict_3.items())

# 1. Do dictionaries keep an order? How do I print the values of the dictionary in order?

# Dictionaries are mappings and do not retain order! If you do want the capabilities of a dictionary 
# but you would like ordering as well, check out the ordereddict object lecture later on in the course!
