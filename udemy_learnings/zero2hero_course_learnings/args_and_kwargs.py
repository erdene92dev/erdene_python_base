# ### args = arguments
# ### the following func take all the parameters entered by a user
# def add_args(*args):
# 	total_arg_value = sum(args)
# 	try:
# 		for count, _ in enumerate(args):
# 			print('item:',_, 'index:',count)
# 		print(f'total sum: {total_arg_value} \ntotal items:',{len(args)})
# 	except ValueError:
# 		return ValueError.___name__
# 	finally:
# 		print('add_args completed in')

# ### add multiple numbers
# print(add_args(10, 25, 5, 10, 3))

# ### kwargs = keyword arguments 
# ### **kwargs works just like *args, but instead of accepting positional arguments 
# ### it accepts keyword (or named) arguments. 
# def myfunc(required, *args, **kwargs):
# 	print(required)
# 	print(args)
# 	print(kwargs)

# myfunc('tony', 'arg1', 'arg2', fruit='fiji apples',veggie='lettuce')


# ### print/return only even args

# def myfunc(*args):
#     even_args = []
#     for par in args:
#         if par % 2 == 0:
#             even_args.append(par)
#     return even_args
#     # print(even_args)
# myfunc(1, 2, 3, 4)


### convert arguments to lower case if its index is odd
def myfunc(*args): 
    return_string = ""
    for index, value in enumerate(*args):
    	# print(index, value)
    	if index % 2 != 0:
    		return_string += value.lower()
    	else:
    		return_string += value.upper()
    return(return_string)

print(myfunc('Anthropomorphis'))


# example of kwarg key/value pair creation and use case case
def mykwargs(**data):
	if data.get('age') > 19:
		for key, value in data.items():
			return(f'{key} is {value}')

print(mykwargs(FirstName='Clark', LastName='Kent',UserName='ckent2015',age=35))
print(mykwargs(FirstName='Anthony', LastName='Stark',UserName='ironman08',age=23))
print(mykwargs(FirstName='Anthony', LastName='Erdene',UserName='ironman08',age=29))