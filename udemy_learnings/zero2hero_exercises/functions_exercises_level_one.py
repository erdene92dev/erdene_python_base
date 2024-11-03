# # -----------------Level 1------------------------- #
# ### Functions Practice Exercise 4:
# ### OLD MACDONALD: Write a function that capitalizes the first and 
# ### fourth letters of a name 

# def capitalize_first_fourth(name):
# 	string = ''
# 	for index, letter in enumerate(name):
# 		# print(index, letter)
# 		if index == 0 or index == 3:
# 			string+=letter.upper()
# 		else:
# 			string+=letter
# 	print(string)
# capitalize_first_fourth('macdonald')


# # --------------------------------------------------- #
# ### Functions Practice Exercise 5:
# ### MASTER YODA: Given a sentence, return a sentence 
# ### with the words reversed
# def sentence_reverse(string_to_reverse):
# 	words = string_to_reverse.split()
# 	reversed_words = []
# 	for _ in words:
# 		reversed_words.insert(0, _)
# 	print(" ".join(reversed_words))
# # check
# sentence_reverse('i am home')
# # check
# sentence_reverse('we are home')

# # v2
# def sentence_reverse_v2(sentence):
# 	words = sentence.split()
# 	reversed_words = words[::-1]
# 	return(" ".join(reversed_words))


# # --------------------------------------------------- #
# # ### Functions Practice Exercise 6:
# ### ALMOST THERE: Given an integer n, return True 
# ### if n is within 10 of either 100 or 200

def almost_there(n):
	offset = 10
	if n >= (100 - offset) and n <= (100 + offset):
		return True
	elif n >= (200 - offset) and n <= (200 + offset):
		return True
	else:
		return False
# check 
print(almost_there(104))

# check 
print(almost_there(150))

# check
print(almost_there(209))