# -----------------warm up------------------------- #
### Functions Practice Exercise 1:
### LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers 
### if both numbers are even, but returns the greater if one or both numbers are odd
def lesser_of_two(a, b):
	if a < b and a % 2 == 0 and b % 2 == 0:
		return a
	elif a > b and a % 2 == 0 and b % 2 == 0:
		return b
	elif  a % 2 != 0 or b % 2 != 0:
		if b > a:
			return b
		else: 
			return a

# check 
print(lesser_of_two(2, 5))

# check 
print(lesser_of_two(2, 4))


# check 
print(lesser_of_two(6, 8))

# check 
print(lesser_of_two(3, 9))

# --------------------------------------------------- #
### Functions Practice Exercise 2: 
### Animal Crackers
### Write a function takes a two-word string and returns True 
### if both words begin with same letter
def same_starting_letter(words):
	count_of_words = len(words.split())
	first_word = words.split()[0]		
	second_word = words.split()[1]
	if count_of_words == 2:
		if first_word.lower()[0] == second_word.lower()[0]:
			print(True)
		else:
			print(False)
	else:
		print(False)

# check
same_starting_letter('United Unicorn')

# --------------------------------------------------- #
### Functions Practice Exercise 3: 
### MAKES TWENTY: Given two integers, return True 
### if the sum of the integers is 20 or if one of the integers is 20. 
### If not, return False
def makes_twenty(required_integer, required_integer2):
	if int(required_integer) + int(required_integer2) == 20 or int(required_integer) == 20 or int(required_integer2) == 20:
			return True	
	else:
		return False
# check 
print(makes_twenty(1, 19))

# check
print(makes_twenty(20,1))

# check
print(makes_twenty(13, 18))

# check
print(makes_twenty(2, 5))