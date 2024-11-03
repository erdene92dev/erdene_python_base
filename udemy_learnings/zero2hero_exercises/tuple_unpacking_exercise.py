# # tuple exaple
# # GET APPLE, BESTBUY, GOOGLE STOCK PRICES 
# # add all the prices and get the total portfolio value
# ticker_list = [('AAPL',175),('BBY',96.08),('GOOGL',2829.53)]
# stock_values = []
# tickers = []

# ### tuple unpack
# for ticker, price in ticker_list:
#     tickers.append(ticker)
#     stock_values.append(price)
#     total_value = round(sum(stock_values))
# print(f'these are the {tickers} tickers in stock price list, total value of stock= {total_value}')

# print('\n')

# ### dictionary unpack
# employee_dict1 = {'user_id':10002, 'date_hired':'2021-01-01', 'salary':69999,'location':'San Francisco', 'state':'CA','country':'USA'}

# ### iterating through key and values
# for key, value in employee_dict1.items():
#     print(key,'->', value,'\n')


# ### iterating through keys
# print('iterating through key example')
# for key, value in employee_dict1.items():
#     print(key)

# ### iterating through values
# print('\niterating through values example')
# for key, value in employee_dict1.items():
#     print(value)


### unpack employee name and hour tuple and capture the employee of the month based on 
### number of hours worked and thanks received


work_hours1 = [('able',10067),('john',50000),('will',1000)]
work_hours2 = [('lebron',20000),('curry',5000),('richardson',1000)]

def employee_of_month(work_hours):
    current_max = 0
    employee_name = ''

    for employees_name, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_name = employees_name
        else:
            pass
    return (employee_name, current_max)

result_wkhr1 = employee_of_month(work_hours1)
result_wkhr2 = employee_of_month(work_hours2)
print(result_wkhr1)
print(result_wkhr2)

# using lambda
def employee_of_month(work_hours):
    return max(work_hours, key=lambda x: x[1])

print(employee_of_month(work_hours2))

### function that multiplies two ints given bound
# def multiply(a, b, bound):
#     if (a * b) <= bound:∫
#         print(a * b)
#         return (a * b)
#     elif (a * b) > bound:
#         raise ValueError(f'multiplication of {a} and {b} with bound {bound} not possible')

# multiply(1, 1, 2)