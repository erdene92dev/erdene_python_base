from datetime import datetime

# get todays date and trunc it to the beginning of the month
datex = datetime.today().replace(day=1)
date_str1 = datex.strftime('%m/%d/%Y')
print("Hello World, the beginning of the current month is: " + date_str1 + '\n')

my_num_list1 = [1, 2, 3, 4, 5]
print('My num_list1:')
print(my_num_list1)

my_var_list = [100, 1.0, 'apple', 5, 'pie']
print('\nMy variables list:')
print(my_var_list)

# you can count the total of items in a list using the "len" function
print("\nThe total count of numbers in my_list1:")
print(len(my_num_list1))

# you can index characters and change them as well
#. change the number "1" in your num list to CAPITAL Number Word"ONE"
print("\nIndex change test on num_list1:")
my_num_list1[0]='ONE ALL CAPS'
print(my_num_list1)

# you can Append / Add items to lists
# add 6 into your num list
print("\nMy append test:")
my_num_list1.append(6)
print(my_num_list1)


# you can Pop / Remove items from a list
# remove the number "6" from your num list 
my_num_list1.pop(5)
print("\nPop test on num_list1:")
print(my_num_list1)


# we can also do loop to del multiple indexes
print("\ndel indexes(Loop) test on var_list:") 
indexes_to_del= [2, 4]
for index in sorted(indexes_to_del, reverse=True):
	del my_var_list[index]

print(my_var_list) 

# you can also sort list in alphabetical or numerical asc/desc
# create a random numbers list and sort it 
my_num_list2 = [100,80,120,4,14]
print("\nSort random integers list test:")
print(my_num_list2)
my_num_list2.sort()
# storing sorted num list with diff name
my_new_sorted_num_list=my_num_list2
print(my_num_list2)
print(my_new_sorted_num_list)

#reverse integer list

print("\nReverse list test:")
my_num_list2.reverse()
reversed_num_list2=my_num_list2
print(reversed_num_list2)



