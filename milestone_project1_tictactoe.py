from pandas import pandas as pd
import numpy as np

### TicTacToe Integer Array limit
valid_index_range = [x for x in range(1,10)]
### test
# print(valid_index_range)

user_one_symbol = ''
# capture users' symbols
while user_one_symbol not in ('X','O'): 
	user_one_symbol = input("Tic Tac Toe Game \nPlayer One : Please Choose 'X' or 'O' as your symbol!: ")

def user_index_choice():
	# initial
	int_isnum = False
	num_in_range = False

	while int_isnum == False or num_in_range == False:
		initial_choice = input('Please pick an index number shown on the game board above: ')
		# check if choice is an integer
		if initial_choice.isdigit() == True:
			# check if choice is in the required integer range
			if int(initial_choice) in range(1,10):
				int_isnum = True
				num_in_range = True
				return int(initial_choice)
			# notify user if integer is outside required range
			elif int(initial_choice) not in range(1,10):
				print(f'Sorry, integer {initial_choice} is outside the required integer window (1 to 9), please try again!')
		# notify user if integer is not an integer type
		elif initial_choice.isdigit() == False:
			print(f'Sorry, {initial_choice} is not a valid integer type, please try again!')

### convert tic_tac_toe dictionary to a DataFrame
### and show tic_tac_toe as a game board table
def show_ttt_table(dict_a):
	print('Tic Tac Tac Table:')

	ttt_DfObj = pd.DataFrame(dict_a, index=['row1', 'row2', 'row3'])
	### show tic tao toe DataFrame "Df"
	print(ttt_DfObj)


# ### display board ex 2
# def display_board(board):
# 	print(board[7], board[8], board[9])
# 	print(board[6], board[5], board[4])
# 	print(board[3], board[2], board[1])


# board_v2 = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']

# display_board(board_v2)


### determine total available cells left to mark by users
def count_cells(dict_a):
	### Initiate Cell Count
	total_cells_marked = 0
	total_cells = 9
	for key, value in ttt_dict.items():
		for x in value:
			if x.isdigit() == False:
				total_cells_marked+=1
				total_cells = total_cells-1
	# for testing
	# print('total cells marked by users:', total_cells_marked)
	# print('total cells left:',total_cells)
	# return {'total_cells':total_cells, 'total_marked_cells':total_cells_marked}
	return total_cells


## determine if user two is the winner:
def user_win_eval(dict_a, user1_symbol):
	user_two_symbol = list(map(lambda user_one: 'O' if user_one == 'X' else 'X', user1_symbol)) 
	user_two_symbol = user_two_symbol[0]
	user1_symbol = user_one_symbol

	diagonal_value_1 = [dict_a['COL1'][0], dict_a['COL2'][1], dict_a['COL3'][2]]
	diagonal_value_2 = [dict_a['COL3'][0], dict_a['COL2'][1], dict_a['COL1'][0]]
	row1_values = [dict_a['COL1'][0], dict_a['COL2'][0], dict_a['COL3'][0]]
	row2_values = [dict_a['COL1'][1], dict_a['COL2'][1], dict_a['COL3'][1]]
	row3_values = [dict_a['COL1'][2], dict_a['COL2'][2], dict_a['COL3'][2]]
	col1_values = [dict_a['COL1'][0], dict_a['COL1'][1], dict_a['COL1'][2]]
	col2_values = [dict_a['COL2'][0], dict_a['COL2'][1], dict_a['COL2'][2]]
	col3_values = [dict_a['COL3'][0], dict_a['COL3'][1], dict_a['COL3'][2]]

	## for testing / qa
	# print('diagonal left to right',diagonal_value_1)
	# print('diagonal right to left',diagonal_value_2)
	# print('first row values', row1_values)
	# print('second row values', row2_values)
	# print('third row values', row3_values)
	# print('COL1 values', col1_values)
	# print(col1_values.count('X'))
	# print('COL2 values', col2_values)
	# print('COL3 values', col3_values)

	winner_id = ''

	if diagonal_value_1.count(f'{user1_symbol}') == 3 or diagonal_value_2.count(f'{user1_symbol}') == 3 or \
	row1_values.count(user1_symbol) == 3 or row2_values.count(f'{user1_symbol}') == 3 or row3_values.count(f'{user1_symbol}') == 3 or \
	col1_values.count(f'{user1_symbol}') == 3 or col2_values.count(f'{user1_symbol}') == 3 or col3_values.count(f'{user1_symbol}') == 3:
		winner_id = '1'
	
	elif diagonal_value_1.count(f'{user_two_symbol}') == 3 or diagonal_value_2.count(f'{user_two_symbol}') == 3 or \
	row1_values.count(f'{user_two_symbol}') == 3 or row2_values.count(f'{user_two_symbol}') == 3 or row3_values.count(f'{user_two_symbol}') == 3 or \
	col1_values.count(f'{user_two_symbol}') == 3 or col2_values.count(f'{user_two_symbol}') == 3 or col3_values.count(f'{user_two_symbol}') == 3:
		winner_id = '2'

	return winner_id

### for testing
# show_ttt_table(ttt_dict)

# print(user_win_eval(ttt_dict))

def user_two_selection(dict_a, user1_symbol):
	user_two_symbol = list(map(lambda user_one: 'O' if user_one == 'X' else 'X', user1_symbol)) 
	user_two_symbol = user_two_symbol[0]
	while user_win_eval(dict_a, user_one_symbol) not in ('1','2'): 
		print('\n'*50)
		show_ttt_table(dict_a)
		print("Hello User '2'!")
		user_index_selection = str(user_index_choice())
		for key, values in dict_a.items():
			index_loc = ''
			### determine if user selection is in within dictionary values
			if user_index_selection in values:
				### if user election is found in dict, get the key and index where
				### users selection is located in 
				### change it to X for user 1 
				dict_a[key][values.index(user_index_selection)] = user_two_symbol
		user_one_selection(dict_a, user1_symbol)

def user_one_selection(dict_a, user1_symbol):
	print('\n'*50)
	show_ttt_table(dict_a)
	while user_win_eval(dict_a, user_one_symbol) not in ('1','2'): 
		print("Hello User '1'!")
		user_index_selection = str(user_index_choice())
		# test
		# user_index_selection = '2'

		for key, values in dict_a.items():
			index_loc = ''
			### determine if user selection is in within dictionary values
			if user_index_selection in values:
				### if user election is found in dict, get the key and index where
				### users selection is located in 
				### change it to X for user 1 
				dict_a[key][values.index(user_index_selection)] = user1_symbol

		# go to user 2 
		user_two_selection(dict_a, user1_symbol)


### determine winner
def game_winner(dict_a):
	if user_win_eval(dict_a, user_one_symbol) is not None:
		winner = user_win_eval(dict_a, user_one_symbol)
	print('\n')
	show_ttt_table(dict_a)
	print(f'Game Over, winner is player {winner}!')
	return winner

### ask user if they want to continue game 
def play_again(dict_a):
	print('\n')
	#if there is a winner, ask if the players want to replay the game
	user_game_choice = input('Continue Game?, enter (Y, Yes, N, No): ')
	
	while user_game_choice.lower() not in ('yes','y','no','n'):
		user_game_choice = input('invalid entry!,  enter (Y or Yes) to play again | or | enter (N or No) to end game: ')	

	while user_win_eval(dict_a, user_one_symbol) is not None:
		if user_game_choice.lower() in ('n','no'):
			print('Thanks for Playing! Game Over')
			break
		elif user_game_choice.lower() in ('y','yes'):
			print('\n'*10)
			game_init()

def game_init():
	### Initate Tic Tac Toe Table : Global
	dict_a = {
	'COL1' : ['1','4','7'],
	'COL2' : ['2','5','8'],
	'COL3' : ['3','6','9'],
	}
	# while a winner is not found
	while user_win_eval(dict_a, user_one_symbol) not in ('1','2'): 
		
		# ask user one		
		user_one_selection(dict_a, user_one_symbol)
	else:
		game_winner(dict_a)
		play_again(dict_a)

game_init()