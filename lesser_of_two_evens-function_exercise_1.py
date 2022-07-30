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