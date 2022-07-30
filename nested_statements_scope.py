## orders of operation 

x = 25

def myfunc():
	x = 50
	return x 

print(myfunc())
print(x)


# per stated code above, 
# x = 25 do not get overriden by myfunc.
# how does python know which x assignment 
# the user is referring to in code?
# python follows a set of built-in rules that enable
# variable assignment by order, called "LEGB" 


# LEGB stands for:
# L stands for Local -- Names assigned in anyway with a function (e.g. def or lambda), and not declared global in that function
# E stands for Enclosing function locals -- Names in the local scope of any and all enclosing functions (def or lambda), from inner to outer 
# G stands for Global (module) -- Names assigned at the top-level of a module file, or declared global in a def within the file 
# B stands for Built-in (Python) -- Names preassigned in the built-in names module : open, range, SyntaxError,....

### see example, the name variable follows the order of assignment mentioned above 

# Global Name
name = 'Anthony'

def greet():
	# Enclosing Name
	name = 'Tony'
	def hello():
		# Local Name
		name = 'Erdene' 
		print(f'Hello {name}, welcome to Sublime')
	hello()
greet()

