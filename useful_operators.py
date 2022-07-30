print('range operator: creates a number range, not including last num. e.g. basic num generator') 
# # range(stop)
# # range(start,stop,step[])

# # print from 0 to 10, step by 2, start from 0 to get even numbers in range
print('range example 1')
for x in range(0,12,2):
	print(x)

print('\nrange example 2:')
# # print from 1 to 15, step by 2, start from 1 to get odd numbers in range
for x in range(1,17,2):
	print(x)
print('\nrange example 3:')

# # create a list using range
# # very efficient way to generate range, instead of stored value
num_range1 = list(range(0,120,20))
print(num_range1)

print('\nregular for loop indexing example:')
index_count = 0
letters = 'abcdefg'
for x in letters:
	# if this index calc is placed on top of the print, index will start at "1"
	# index_count+=1 
	print('index at {} is the letter {}'.format(index_count, x))
	index_count+=1

# # Rather than creating and incrementing a variable yourself, 
# # you can use Python’s enumerate() to get a counter and the value from the iterable at the same time!
print('\nenumerate indexing example: add counter to each of the letters in "word"')
word = 'International'
for x in enumerate(word):
	print(x)

print('\nenumerate with tuple unpacking example:')

for position_value, letter in enumerate(word):
	print('the index of {} is the letter {}'.format(position_value, letter))

print('\nenumerate with tuple unpacking example 2:')
word2 = 'Dagiimaa'

for i, l in enumerate(word2):
	print('the index of {} is the letter {}'.format(i, l))


print('\nzip example 1')
num_list1 = [1, 2, 3, 4, 5, 6]
var_list1 = ['a','b','c','d','e','f']
sum_list1 = [100,250,50,500,600,25]
new_tuple_list = zip(num_list1, var_list1, sum_list1)

print('new tupe list stored in memory:', new_tuple_list)
for item in new_tuple_list:
	print(item)

print('\nin example:')
# # in function can check if variable is in a container iterable object
print('x' in var_list1)
print(6 in num_list1)
# # in function can check if variable is in a string
print('z' in 'international')
# # in function can check if a key is in a dictionary
my_dict =  {'k1':'new york','k2':100, 'k3':'XYZ'}
print('k2' in my_dict)
# # in function can check if a key value is in a dictionary
print('XYZ' in my_dict.values())