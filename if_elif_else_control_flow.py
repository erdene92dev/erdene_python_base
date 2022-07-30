# Control Flow, use logic to execute certain code when a particular condition has been met
# ex, if country = US, then rev = 100

dog_hungry_bool = input("Is your dog hungry or no: ")

if dog_hungry_bool.lower()=="yes":
	print("Feed your dog some chum chums\n")
else:
	print("Dog is not hungry\n")


curr_loc = input("Please enter user location:")
bank_calc = 50*2
test_case ="User location test:"
if curr_loc =='Auto Shop':
	print(test_case)
	print("User is at Auto Shop")
elif curr_loc =="Bank":
	print(test_case)
	print("User is at the bank, and he withdrew:",bank_calc)
elif curr_loc =='Restaurant':
	print(test_case)
	print("User is at the Restraunt")
else:
	print(test_case)
	print("User loc is unknown")


name = input("Please enter your name: ")

if name.lower() == "anthony":
	print("Hello " + name + ",pleasure to meet you")
elif name.lower() != "anthony":
	print("You are not the user of this computer, please enter your name: ")
	new_name = input()
	print("Hello " + new_name)