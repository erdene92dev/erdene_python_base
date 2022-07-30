# import math
# import string

# ### Homework question 1:
# ### Write a function that computes the volume of a sphere given
# ### its radius
# ### The volume of a sphere is given as: 4/3*pi*radius**3

# print('hw 1; determine volume of a sphere given its radius.')
# def vol(rad):
# 	return (4/3)*math.pi*rad**3
 

# # check 
# print(vol(2))

# # --------------------------------------------------- #
# ### Homework question 2:
# ### Write a function that checks whether a number is 
# ### in a given range (inclusive of high and low)
# print('\nhw 2; check if num is in specified range.')
# def range_check(num,low,high):
# 	if num > low and num < high:
# 		return (f'{num} is in the range between {low} and {high}.')
# 	else:
# 		return (f'{num} is NOT in the range between {low} and {high}.')

# def ran_bool(num, low, high):
# 	if num > low and num < high:
# 		return True
# 	else:
# 		return False

# # check
# print(range_check(2, 10, 15))
# print('bool check 1:',ran_bool(2, 10, 15))

# # check
# print(range_check(2, 1, 5))
# print('bool check 2:',ran_bool(2, 1, 5))
# # check
# print(range_check(5, 2, 7))
# print('bool check 3:',ran_bool(5, 2, 7))


# # --------------------------------------------------- #
# ### Homework question 3:
# ### Write a Python function that accepts a string and calculates the 
# ### number of upper case letters and lower case letters.
# print('\nhw 3; calc lower and upper case chars in a given string.')

# def string_case_count(string):
# 	lower_letter_count=0
# 	upper_letter_count=0
# 	words = [x for x in string.split()]
# 	# for every word in words
# 	for _ in words:
# 		# for every letter in each word
# 		for _ in _:
# 			if _ .isalpha() == True and _.islower()==True:
# 				lower_letter_count+=1
# 			elif _ .isalpha() == True and _.isupper()==True:
# 				upper_letter_count+=1
# 	return(f'No. of Upper case characters : {upper_letter_count} \
# 		\nNo. of Lower case characters : {lower_letter_count}')
# # check
# print(string_case_count('Hello Mr. Rogers, how are you this fine Tuesday?'))


# # --------------------------------------------------- #
# ### Homework question 4:
# ### Write a Python function that takes a list and returns a 
# ### new list with unique elements of the first list.
# print('\nhw 4;')
# def unique_list(src_lst):
	
# 	src_lst = set(src_lst)
# 	return (src_lst)
# # check
# print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))
# # check
# print(unique_list(['alpha','delta','alpha2', 'delta']))

# --------------------------------------------------- #
### Write a Python function that checks whether a word or phrase 
### is palindrome or not. Palindrome are words that read the same backwards as forward
## Homework question 5:
print('\nhw 5; is word or phrase palindrome')


def palindrome(string):
	# lower every letter in word
	string = string.lower()
	if string[::-1] == string:
		return True
	
print(palindrome('hel  leh'))
print(palindrome('Madam'))
print(palindrome('racecar'))
print(palindrome('civic'))



# # --------------------------------------------------- #
# ### Write a Python function to check whether a string is pangram or not.
# ### (Assume the string passed in does not have any punctuation)
# print('\nhw 6; is string a pangram, e.g. contain all the letters in the alphebet')
# alphabet_string = string.ascii_lowercase
# alphabet_list = sorted(list(alphabet_string))

# def ispangram(string):	
# 	print('alpha:',alphabet_list)
# 	print('given string:', string)
# 	# lower all words in string
# 	og_string = string.lower()
# 	# remove all spaces
# 	og_string = og_string.replace(' ','')
# 	# capture all the letters given in a string
# 	letters = []
# 	missing_letters = []
# 	string_is_pangram = False
# 	for words in og_string:
# 		for l in words:
# 			letters.append(l)
# 	# deduplicate given letters into a unique list 
# 	unique_letters_in_string = sorted(list(set(letters)))
# 	# return ('letters from string:', unique_letters_in_string)
# 	# # check if all the letters match ascii_lowercase letters, a-z
# 	for index, letter in enumerate(alphabet_list):
# 		if letter not in unique_letters_in_string:
# 			missing_letters.append(letter) 
# 		elif letter in unique_letters_in_string and len(alphabet_string) == len(unique_letters_in_string):
# 			string_is_pangram = True
# 			return(f'string is a pagram, all letters in the alphabet found.')
	
# 	while string_is_pangram == False:
# 		return(f'string is not a panagram, because {missing_letters} is missing ')

# 		# bool check
# 		# if letter == alphabet_list[index]:
# 		# 	letter_bool.append(True)
# 		# else:
# 		# 	letter_bool.append(False) 


# print(ispangram("The quick brown fox jump over the lazy"))


# # --------------------------------------------------- #
# # Write a function that multiplies each number and gets the total
# print('\nhw 7; multiple each number in a given num list')
# def multiply(nums):
# 	total = 1
# 	for _ in nums:
# 		total = _*total
# 	return total
# # check
# print(multiply([2*2*2]))