### LABMDA : MAP EXPRESSION, run a function on an iterable object
print('multiplication example using map and function:')
def times_two(x):
	return x*2
num_list = [1, 2, 3, 4, 5, 6]

### implement function times_two() on every integer within
### num_list via map()
for num in map(times_two, num_list):
	print(num)

print('\nsum all numbers after multiplication using list comprehension ex:')
total_sum = sum([x for x in map(times_two, num_list)])
print(total_sum)


### FILTER function extracts elements from an iterable (list, tuple, dic etc.) 
### for which a function returns True 

def check_even(x):
	if x % 2 == 0:
		return True
	return False

### extract only even numbers from num_list
evens_list = filter(check_even, [x for x in num_list])

print('\nevens filter check on num_list example 1:')
for _ in evens_list:
	print('found even:',_)


### lambda expressions are anonymous functions 
### lamdda expressions does not require naming
### lambda expressions saves spaces when a function needs to be used once
### if a function needs to be used more than once, then def function is preferred
print('\nmultiplication example via lambda and map method, \
	\ncapture the total sum of num list after multiplying each number \
	\nby 2 via the lambda and map method:')
sum_output2 = sum(map(lambda times_two: times_two * 2, num_list))
print(sum_output2)


### lambda expression: check even
print('\nlambda example 2, check even:')
even_output2 = list(filter(lambda even: even % 2 == 0, num_list))
print(even_output2)


### labmda expression: grab first character from name list
print('\nlambda example 3: first char')
name_list=['Anthony','Erdene','Dagiimaa','Isaac']
first_char = list(map(lambda first_char: first_char[0], name_list))
print(first_char)