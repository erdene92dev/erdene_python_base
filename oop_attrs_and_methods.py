### Object Oriented Programing is referred to as OPP
### OOP allows users to create their own objects that have customed functions in them
### functions within classes() are more repeatable, scalable, and look more organized, hence, easy to refer to

# OOP example Dog that has the function breed given user input

class MyDog():

	### CLASS OBJECT ATTRIBUTE
	### SAME FOR ANY INSTANCE OF A CLASS
	species = 'canine'

	def __init__(self, breed, name, weight, spots):
		# Attributes: acronym = attrs
		# we take in the arguments/attrs
		# assign it using self.attribute_name
		self.breed = breed
		self.name = name
		self.weight = weight

		# expect bool
		self.spots = spots

df_dog = MyDog(breed='Husky', name='Miko', weight=100, spots=False)

## get dog breed
print(df_dog.breed)
## get dog name
print(df_dog.name)

## gets dogs weight
print(df_dog.weight)
## check if dog has spots or not, bool, true or false
print(df_dog.spots)

print(df_dog.species)


