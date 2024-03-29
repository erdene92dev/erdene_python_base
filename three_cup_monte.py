from random import shuffle
from datetime import datetime, date

print(datetime.today())

### initialize ball list aka cups_n_balls, place ball "O" in position
ball_list = ['', 'O','']

### custom shuffle and return:
### shuffle will not return assignment when used in same line
def shuffle_list(mylist):
	shuffle(mylist)
	return mylist

### acquire and verify if user input is in "int" type
def get_user_input():
	try:
		user_input = int(input('please pick a number from 1, 2, 3:'))
		if user_input in ["quit","q"]:
			pass
		else:
			return user_input
	except ValueError:
		print(f'Failed with exception {ValueError.__name__}, you did not make a valid entry,\ntry again.')
	except TypeError:
		print('You did not enter a valid entry, please try again.')

### acquire and verify user index choice and determine if its a valid index selection
### if its not a valid selection, loop until valid index selection is made and exit
def user_index_evaluation():
	print('Welcome to "Three Cup Monte" in Python. \nThe numbers 1, 2, 3 are cups,\
 please guess the cup that contain the ball.')
	index_guess = get_user_input()	
	index_tuple = (1, 2, 3)
	is_index_valid = index_guess in index_tuple	
	if is_index_valid == True:
		if index_guess == 1:
			return 0
		elif index_guess == 2:
			return 1 
		elif index_guess == 3:
			return 2 
	while is_index_valid == False:
		new_index_guess = get_user_input()
		if new_index_guess in index_tuple:
			is_index_valid == True
			return int(new_index_guess) 

# ---------------------------------------------------------------------------
### for testing only, keep commented. dev check to see if nonetype is existent
# user_index_guess = user_index_evaluation()
# print(user_index_guess)

### check users guess
def check_guess(cups_n_balls, user_index_guess):
	# find where the ball is after shuffle
	if cups_n_balls[user_index_guess] == 'O': 
		print(f'You guessed correct! the ball is indeed in position {user_index_guess+1}.')
		print(cups_n_balls)
	else:
		ball_location = cups_n_balls.index('O')
		# converting starting point 0 to 1 
		ball_index = cups_n_balls.index('O')
		print(f'Wrong guess!, the ball is in position {ball_index+1}.')
		print(cups_n_balls)

### ask user for replay
def ask_for_replay():
	user_request_replay = str(input('Would you like to play again, enter Yes or No:'))
	user_request_replay = user_request_replay.lower()
	
	while user_request_replay not in ['yes','no','exit']:
		user_request_replay = str(input('Would you like to play again, enter Yes or No:')).lower()
	if user_request_replay == 'yes':
		start_game()
	elif user_request_replay == 'no'or user_request_replay == 'exit':
		exit()

def start_game():
	index_value = user_index_evaluation()
	my_shuffled_list = shuffle_list(ball_list)
	check_guess(my_shuffled_list, index_value)
	ask_for_replay()

start_game()