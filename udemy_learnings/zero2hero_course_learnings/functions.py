from datetime import date
import sys
# print python vs
print('python sys version:', sys.version)
print('program run date:', date.today())


# user_full_name_list = []

# ### create a funciton that takes user first and last name
# ### and prints their name along with a welcome statement
# print('function: user greet and data intake \
# 	')
# def capture_user_details():
# 	user_first_name = input('Please Enter Your First Name: ')
# 	user_last_name = input('Please enter Your Last Name: ')
# 	full_name = user_first_name + ' ' + user_last_name
# 	return full_name
# 	print(f'Hello {full_name}, Welcome to Sublime, \
# please enter three integers to add:')
# capture_user_details()



# num_list = []
# even_list = []
# odd_list = []
# ### create a function that adds all the numbers entered by a user by input
# ### and returns the total sum, max 3 numbers
# ### return functions returns the entered variables % modded by 2
# print('function: user number calculation test')
# def add_nums():
# 	while len(num_list) < 3:
# 		user_num = int(input('please enter a number to add:'))
# 		num_list.append(user_num)
# 	print('Hello ,You have entered the following numbers: ',num_list)
# 	total_num_sum = 0
# 	for x in num_list:
# 		total_num_sum += x 
# 	print('total "sum" of numbers = ',total_num_sum)
# 	for x in num_list:
# 		if x % 2 == 0:
# 			even_list.append(x)
# 		elif x % 2 != 0:
# 			odd_list.append(x)
# 	print('these are the odd numbers within your number list', odd_list)
# 	print('these are the even numbers within your number list', even_list)
# add_nums()

### create a function that adds numbers given parameter definition
def add_func(a, b, c):
	print(a+b+c)
	return(a+b+c)
add_func(1, 2, 3)

result = add_func(100,200,400)
