print('test 1:')
# Question 1:
# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this Sentence'

for _ in st.split():
	if _[0].lower()=='s':
		print(_)

print('\ntest 2:')
# Question 2:
# Use range() to print all the even numbers from 0 to 10.

# first way by calc
for _ in range(0,11):
	if _ % 2 == 0:
		print(_)

# second way by using offset function within range
for _ in range(0,11,2):
	print(_)

print('\ntest 3:')
# Question 3:
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

# standard way
print('standard way list creation')
num_range = range(1,51)
num_range_custom = []
for x in num_range: 
	if x % 3 == 0:
		num_range_custom.append(x)
print('divisible by 3 numbers from range 1 to 50:', num_range_custom)

print('\nlist comprehension')

num_range_custom = [x for x in num_range if x%3==0]
print(num_range_custom)

# Question 4
# Go through the string below and if the length of a word is even print "even!"

print('\ntest 4:')
# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'

for _ in st.split():
	if len(_) % 2 == 0:
		print('this word "{}"" has a even length of {}'.format(_, len(_)))

print('\ntest 5:')
# Write a program that prints the integers from 1 to 100. 
# But for multiples of three print "Fizz" instead of the number, 
# and for the multiples of five print "Buzz". 
# For numbers which are multiples of both three and five print "FizzBuzz".
num_list = []
for _ in range(0,101):
	if  _ % 3 == 0 and _ % 5 == 0:
		num_list.append('FizzBuzz')
	elif _ % 3 == 0:
		num_list.append('Fizz')
	elif _ % 5 == 0:
		num_list.append('Buzz')
	else:
		num_list.append(_)
print(num_list) 

print('\ntest 6:')
# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
first_letter_list = []
for _ in st.split():
	first_letter_list.append(_[0])
print(first_letter_list)


first_letter_list = [x[0] for x in st.split()]
print(first_letter_list)
