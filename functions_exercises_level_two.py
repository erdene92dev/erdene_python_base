# # -----------------Level 2------------------------- #
# ### Functions Practice Exercise 7:
# ### Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
# def has33(int_array):
# 	for i in range(0, len(int_array)):
# 		# print(i)
# 		if int_array[i:i+2] == [3, 3] or int_array[i:i+2] == (3, 3):
# 			return True	
# 	return False

# # check
# print(has33((2, 2, 2, 2, 4, 3, 3)))

# # check
# print(has33([1, 3, 3]))

# # check
# print(has33([1, 3, 1, 3]))

# # check
# print(has33([3, 1, 3]))

# # check
# print(has33([3, 3, 1]))


# # --------------------------------------------------- #
# ### Functions Practice Exercise 8:
# ## PAPER DOLL: Given a string, return a string where for every character
# ## in the original there are three characters

# def paper_doll(string):
# 	string_multiplication = [x*3 for x in string]
# 	updated_string = "".join(string_multiplication)
# 	return updated_string
# # check
# print(paper_doll('hello'))

# # # Check
# print(paper_doll('Mississippi'))

# def paper_doll_v2(string):
# 	result = ''
# 	for x in string:
# 		result += x*3
# 	return result

# # check
# print(paper_doll_v2('hello'))

# # --------------------------------------------------- #
# ### Functions Practice Exercise 9:
# ### BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# ### If their sum exceeds 21 and there's an eleven, 
# ### reduce the total sum by 10. 
# ### Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

# def blackjack_v1(a, b, c):
# 	if sum([a, b, c]) < 21:
# 		return(sum([a,b,c]))
# 	elif sum([a, b, c]) == 21 and 11 not in (a, b, c) :
# 		return('Blackjack: 21')
# 	elif 11 in [a, b, c] and sum([a, b, c])-10 < 21:
# 		return sum([a,b, c])-10
# 	elif 11 in [a, b, c] and sum([a, b, c])-10 == 21:
# 		return('Blackjack: 21')
# 	# elif sum([a, b, c]) > 21 and 11 not in [a, b, c]:
# 	else:
# 		return('BUST:' + str(sum([a, b, c])))

# # check
# print(blackjack_v1(7, 7, 7))
# # check 
# print(blackjack_v1(7, 11, 7))
# # Check
# print(blackjack_v1(5, 6, 7))
# # Check
# print(blackjack_v1(9, 9, 9))
# # Check
# print(blackjack_v1(9, 9, 11))
# # check
# print(blackjack_v1(10,10,11))

# # --------------------------------------------------- #
# # ### Functions Practice Exercise 9:
# ### SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 12 
# ### and extending to the next 20 (every 6 will be followed by at least one 9). Return 0 for no numbers.

# def summer12(arr):
# 	total_sum = 0
# 	add = True

# 	for num in arr:
# 		while add:
# 			if num != 12:
# 				total_sum += num
# 				break
# 			else:
# 				add = False
# 		while add == False:
# 			if num != 20:
# 				break
# 			else:
# 				add = True
# 	return total_sum

# print(summer12([1, 12, 13, 14, 20, 5]))