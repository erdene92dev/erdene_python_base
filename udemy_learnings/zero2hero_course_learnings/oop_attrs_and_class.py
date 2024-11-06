### Object Oriented Programing is referred to as OOP
### OOP allows users to create their own objects that have 
### customizedd functions in them
### functions within classes() are more repeatable, scalable, 
### and look more organized, hence, easy to refer to

# # OOP example "pizza"

class Pizza_Order():
    # CLASS OBJECT ATTRIBUTE
    food_type = 'Pizza'

    def __init__(self, size, toppings, delivery=bool): 
        self.size = size
        self.toppings = toppings
        self.delivery = delivery
    
    # Operations / Actions -----> Methods
    
    # Calculate Pizza Order Method
    def order_total(self): 
        order_total = 0
        size_cost = 0
        toppings_cost = 0
        delivery_cost = 10

        pizza_size_type = (self.size).lower()

        if pizza_size_type == 'large': 
            size_cost = 15
        elif pizza_size_type == 'medium':
            size_cost = 12.50
        elif pizza_size_type == 'small': 
            size_cost = 10

        # charge 0.75 cents for each pizza topping
        toppings_cost = 0.75*(len(self.toppings))

        if self.delivery==False: 
            delivery_cost = 0
        else: 
            delivery_cost = 20
        
        order_total = size_cost + toppings_cost + delivery_cost
        return order_total
    
    def order_printout(self): 
        print('Pizza Size:', self.size)
        print('Pizza Toppings:', self.toppings)
        print('Order Takeout:', self.delivery)


pizza_order_no1=Pizza_Order('Large',('pepperoni','ham','veggies'), delivery=True)
pizza_order_no2=Pizza_Order('Small',('ham','sausage','pineapple','anchovies'), delivery=True)

print('My First Pizza Order Details:')
pizza_order_no1.order_printout()
print('Total Cost of Pizza:')
print(pizza_order_no1.order_total())

print('\nMy Second Pizza Order Details:')
pizza_order_no2.order_printout()
print('Total Cost of Pizza:')
print(pizza_order_no2.order_total())