# # -----------------Level 3: Challenging------------------------- #
### SPY GAME: Write a function that takes in a list of integers and 
### returns True if it contains 007 in order

# def spy_game(nums_list):
# 	index_location_of_ints = [_ for _ in range(len(nums_list))]
# 	index_location_of_zeroes = []
# 	# find index location of zeroes for calc
# 	for i in index_location_of_ints:
# 		if nums_list[i] == 0:
# 			index_location_of_zeroes.append(i)
# 	# determine if there is a 007 in the num list
# 	for index, nums in enumerate(nums_list):	
# 		if nums == 7 and nums_list[index-2:index] == [0,0]:
# 			return True 
# 		elif nums == 7 and index > min(index_location_of_zeroes) and index > max(index_location_of_zeroes) and len(index_location_of_zeroes) == 2:
# 			return True 
# 	return False
 
# # check
# print(spy_game([1,2,4,0,0,7,5]))

# # check 
# print(spy_game([1,0,2,4,0,5,7]))

# # check 
# print(spy_game([0, 1, 2, 7, 3, 0, 1, 2, 7]))

# # check 
# print(spy_game([0,7,0,7]))


# --------------------------------------------------- #
# Write a function that returns the number of prime numbers that exist up to and including a given number
# prime number is a natural number greater than 1 and it is divisible by itself or 1, hence have a factor of 2 
import math

def count_primes(num):
	# 2 is prime because it can created by the following 2 * 1 and 2 / 1 == 2:
	# no other even numbers can be prime because it can factored by more than 2 times

	# check for 0 or 1 input

	if num < 2:
		return 0

	# 2 or greater
	# store primes
	primes = [2]

	# counter to num
	x = 3

	while x <= num:
		for y in primes:
			# check if x is prime from 3 up to x
			if x % y == 0:
				x+=2
				break
		else:
			primes.append(x)
			x+=2
	print(primes)
	print(len(primes))

count_primes(100)