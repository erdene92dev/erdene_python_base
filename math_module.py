import math as m

# num1 = 4

# ### "factorial" method within math module
# ### formula is n! = n * (n-1)!
# ### factorial of 4 = 4*3, 4*2, 4*1
# print(f'factorial of {num1} = {m.factorial(num1)}')

# def factorial_formula_ex(n):
# 	n_factorial = sum([n*_ for _ in range(n)[::-1]])
# 	return n_factorial

# print(factorial_formula_ex(4))

### gcd method finds the greater common divisor between two numbers
### GCD is also known as the highest common factor (HCF).

print(m.gcd(3, 6))
print(m.gcd(2, 10))
print(m.gcd(2, 4))
print(m.gcd(100, 50))