import math 
import time
import datetime

# % is the modulo operator that  
# finds the remainder
# of a division operator
def is_prime_v1(n):
    if n < 2:
        return False
    for i in range(2, n): 
        if n % i == 0: 
            return False # it is evenly divisible
        return print(f"{n} is a Prime")  

is_prime_v1(7)

is_prime_v1(8)

is_prime_v1(3)
