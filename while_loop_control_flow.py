# While loops continue to execute a block of code 
# while some condition is true

# while test 

x = 0

# while x = 0 add to 5
while x <= 4:

# infinite while loop with x
	# x = x + 1
	x+=1
	print('the current value of x is:', x)
else:
	print("x is not less than 5")

# # statements for additional functionality
# # break: breaks out of the current closest enclosing loop
# # continue: Goes to the top of the closes enclosing loop
# # pass: does nothing at all

list_1 = [1, 2, 3]

for item in list_1:
	# comment: does not work, cause EOL error
	# pass allows the code to run, very useful for placeholder
	pass

mycustom_string = 'Anthony'

for letter in mycustom_string:
	if letter == 't':
		continue # skips t
	print(letter)

for letter in mycustom_string:
	if letter == 'h':
		break
	print(letter)




# # break at number 6
print('\nbreak using num_list ex:')
newnum_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in newnum_list:
	if num == 6:
		break
	print(num)