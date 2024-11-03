from datetime import datetime, date

print('todays date:',date.today())

# ### function that takes number input from user 
# ### and determines if it is even or odd number:
# def check_num():
# 	user_num = int(input('\nplease enter a number: '))
# 	if user_num % 2 == 0:
# 		print(f'{user_num} is an even number.', )
# 	elif user_num % 2 != 0:
# 		print(f'{user_num} is an odd number.')
# check_num()

# print('\nis 5 an even number:', check_even(5))

# ### list dedup using set() function
# num_list = [1001, 2002, 4000, 92, 92, 4000, 1001]
# print('\nmy original num list:', num_list)
# num_list = set(num_list)
# num_list = sorted(num_list,reverse=False)

# print('num list after dedup in ascending order:', num_list)

### print only the vowels from your name using list comprehension
lower_case_vowels = ['a', 'y', 'i', 'o', 'u', 'e', 'w']
upper_case_vowels = [x.upper() for x in lower_case_vowels]

def vowel_check_on_user_name():
	### Try It: change test name to your name
	# test_name = 'Thomas Anderson'
	test_name = input('\nplease enter your name: ')
	vowel_list = [_ for _ in test_name if _ in lower_case_vowels or _ in upper_case_vowels]
	### unify all vowels into distinct, lowercase vowels to get exact vowel count 
	vowel_list = set([_.lower() for _ in vowel_list])
	vowel_list = sorted(vowel_list, reverse=False)
	vowel_count = len(vowel_list)
	print(
		f'you have  {vowel_count} vowels in your name "{test_name}", they are {vowel_list}')
vowel_check_on_user_name()

# ### function that checks if a number is even or not
# def even_check(num):
# 	return num % 2 == 0

# print('the following number is even:', even_check(3))

# ### function that validates if a number is even or odd
# def eval_nums(num_list):
# 	even_list = []
# 	odd_list = []
# 	for _ in num_list:
# 		if _ % 2 == 0:
# 			even_list.append(_)
# 		elif _ % 2 != 0:
# 			odd_list.append(_)
# 	if len(odd_list) > 0 and len(even_list) > 0:
# 		even_and_odd = even_list + odd_list
# 		print(f'user entered odd {odd_list} "and" even {even_list} numbers.')
# 		return even_and_odd
# 	elif len(odd_list) > 0 and len(even_list) == 0:
# 		print(f'user entered only "odd" {odd_list} numbers.')
# 		return odd_list
# 	elif len(odd_list) == 0 and len(even_list) > 0:
# 		print(f'user entered only "even" {even_list} numbers.')
# 		return even_list
	
# eval_nums([1, 3, 9, 2, 8, 12, 14, 16])
# eval_nums([3, 3, 3])
# even_tuple = (24, 84, 64)
# eval_nums(even_tuple)