
# # # for loops allow custom code excecution while
# # # certain elements exist in a iterable object

# # # e.g., you can iterate over every character in a string
# # # iterate over every every item in a list
# # # iterate over every key in a dictionary

# # # syntax of a for loop
# my_iterable_object = [1, 2, 3]
# for x in my_iterable_object:
# 	print(x)

# # get even or odd number program example using for loop
# my_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print('my_num_list=', my_num_list)
# user_input_box_value = input(
#     "Do you want odd or even numbers from my_num_list:")
# odd_array = []
# even_array = []

# def ask_user_num_ex():
#     if user_input_box_value.lower() == 'even':
#         for x in my_num_list:
#             if x % 2 == 0:
#                 even_array.append(x)
#         print('These are the even numbers in my_num_list:', even_array)
#     # print('This are the even number in an array:',even_array)
#     elif user_input_box_value.lower() == 'odd':
#         for x in my_num_list:
#             if x % 2 == 1:
#                 odd_array.append(x)
#         print('These are the odd numbers in my_num_list:', odd_array)
#     # print('This are the odd numbers in an array:',odd_array)
#     else:
#         print("Incorrect Selection: please enter 'even' or 'odd'.")

# ask_user_num_ex()

# # standard for loop on tuple
# my_tuple = (1, 2, 3, 4)
# def print_tuple():
# 	for _ in my_tuple:
# 		print(_)

# print_tuple()

# # example of tuple unpacking method
my_tuple_list = [(1,2),(3, 4), (5,6), (7,8),(9,10)] # extremely common

print('example of a tuple list\n',my_tuple_list,'\n')

# check how many items are in the list tuple
item_cnt = len(my_tuple_list)
print('there are', item_cnt,'items in my my_tuple_list.')

# # looping through tuple list example
# # unpack tuple by item
print('\nunpacking tuple_list by tuple')
for _ in my_tuple_list:
	print(_)

# # tuple unpacking
# # grab each element from tuple	
print('\nunpacking tuple_list tuple item')
for (a,b) in my_tuple_list:
	print(a)
	print(b)

# # perform tuple unpacking 3 item tuple
my_tuple_list2 = [(4, 5, 6),(1, 2, 3),(7, 8, 9)]
print('\nmy_tuple_list2=',my_tuple_list2) 
middle_item_in_my_tuple_list2 = []
for a, b, c in my_tuple_list2:
	middle_item_in_my_tuple_list2.append(b)
print('the middle integers within my_tuple_list2 are:',middle_item_in_my_tuple_list2)


print("\nloop and print the 'key' within dict")
d1 = {'k1':1, 'k2':2,'k3':3}

for _ in d1:
	print (_)
	# # python automatically print key names

# # to loop and print the values within the dict
# # we must use the tuple unpacking
print("\nloop and print the 'value' within dict")
for key, value in d1.items():
	print(value)

print("\nloop and print 'key' + 'value' within dict")
for key, value in d1.items():
	print(key, value)