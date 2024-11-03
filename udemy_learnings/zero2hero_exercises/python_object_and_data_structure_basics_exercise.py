import math

intro='Hello, My name is Anthony and this is my \
Section 3: Objects and Data Structure assessment test. \n'
print(intro)

# # # ------------ MATH ------------ # # #
print('MATH:')
print('What is the value of the expression 4 * (6 + 5)?')
test_1_answer = '44\n'
print(test_1_answer)

print('What is the value of the expression 4 * 6 + 5?') 
test_2_answer = '29\n'
print(test_2_answer)

print('What is the value of the expression 4 + 6 * 5?') 
test_3_answer = '34\n'
print(test_3_answer)

print('What is the type of the result of the expression 3 + 1.5 + 4?')
test_4_answer = type((3+1.5+4))
test_4_answer_set = "the date of this equation is : " + str(test_4_answer) + '\n'

print(test_4_answer_set)

print("What would you use to find a number's square root?")

# square root 
# method 1
num1 = 9
print(math.sqrt(num1))
# method 2
print(9**0.5)

print("\nWhat would you use to find a number's square?")
num1_sqr=num1**2
print(num1_sqr)

# # # ------------ STRING ------------ # # #
print("\nSTRING:")
print("Given the string 'hello' give an index command that returns 'e'. Enter your code in the cell below:")
string_1 = 'hello'
print(string_1[1])

print("\nReverse the string 'hello' using slicing:")
print(string_1[::-1])

print("\nGiven the string hello, give two methods of producing the letter 'o' using indexing.")
# METHOD 1 index from start
print(string_1[4])

# METHOD 2 reverse index, index from the back
print(string_1[-1:])


# # # ------------ LISTS ------------ # # #
print("\nLISTS:")
print("Build this list [0,0,0] two separate ways.")
#Method 1:
list_1 = [0,0,0]
print(list_1)

# Method 2:
list_2 = [0]*3
print(list_2)

print("\nReassign 'hello' in this nested list to say 'goodbye' instead:")
list_3 = [1,2,[3,4,'hello']]
list_3[2][2] = 'goodbye'
print(list_3)

list_4=[5,3,4,6,1]

print("\nSort List 4:")
print(sorted(list_4))


# # # ------------ DICTIONARIES ------------ # # #
print("\nDICTIONARIES:")
# # # Using keys and indexing, grab the 'hello' from the following dictionaries:

print("Using keys and indexing, grab the 'hello' from the following dictionaries:Using keys and indexing, grab the 'hello' from the following dictionaries:")
d = {'simple_key':'hello'}
# Grab 'hello'

print("\nGrab 'hello'")
print(d['simple_key'])

# Grab 'hello'
d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])



# Getting a little tricker
d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])



# This will be hard and annoying!
d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

print("\nCan you sort a dictionary? Why or why not?")
print("-No, because normal dictionaries are mappings not a sequence\n")

# # # ------------ TUPLES ------------ # # #
print("\nTuples:")

print("What is the major difference between tuples and lists?")
print("-Tuples are immutable/not changeable")

tuple_1=('tuple_item_one',2,3)
print(tuple_1)

# # # ------------ Sets ------------ # # #
print("\nSets:")
print("What is unique about a set?")
print("-They do not allow multiple entries of the same char\duplicate items.")

list5 = [1,2,2,33,4,4,11,22,3,3,2]
set_list5 = set(list5)
print(set_list5)

# # # ------------ BOOLEANS ------------ # # #
print("\nBOOLEANS:")
print("2>3:",2>3)

print("3<=2:",3<=2)

print("3==2.0", 3==2.0)

print("4**0.5!=2",4**0.5!=2)
