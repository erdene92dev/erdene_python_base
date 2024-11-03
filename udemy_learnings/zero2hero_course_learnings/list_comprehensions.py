# # list creation using a variable via "for loop" and "append" function
# # example 1: string
my_lista = []

my_variable = 'thisisavariable' 

for _ in my_variable:
	my_lista.append(_)
print(my_lista)

# # more efficient way is via list comprehensions
# # by efficient, by taking less space in code, comp time is same
print('\n')
my_lista = [_ for _ in my_variable]
print(my_lista)


# # example 2: string
print('\n')
my_listb=[x for x in 'examplevariabletwo']
print(my_listb)

# # example 3: using range function
print('\n')
my_listc = [num for num in range(0,11)]
print(my_listc)

# # example 4: using 'square' math calculation with range function
# # square root
print('\n')
my_listd = [num**2 for num in range(0,11)]
print(my_listd)

# # example 5: create even number list on the square of range 0 to 10 
print('\n')
my_liste = [x**2 for x in range(0,11) if x%2==0]
print(my_liste)

# # example 6: create vowel list from a string variable using list comprehensions, using if and else function
vowels = ['A', 'E', 'I', 'O', 'U', 'Y', 'W']
# print only the vowels from my_variable_string 
list_c = [x for x in my_variable_string if x.upper() in vowels]
print(list_c)

# # print only the vowels from my_variable_string , else place "not_a_vowel"
# # this way is very confusing and nested, not easily readable in the future
# # code should be written in a way that is easy to and repeatable
test_string = 'unitedstatesofamerica'
list_c = [x if x.upper() in vowels else "not_a_vowel" for x in test_string]
print(list_c)