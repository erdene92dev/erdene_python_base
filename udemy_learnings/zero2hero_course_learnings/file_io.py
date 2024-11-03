from datetime import datetime, date

import sys

print('current py sys vs:', sys.version)
print("today's date is:", date.today())


# open file
my_file = open('/Users/anthonyerdene/Documents/personal_data/sw_ds_de_dev/python_dev/test_files/example_transactions.csv','r')

print(my_file.name)
print(my_file.mode)


# close file
my_file.close()	
# check if file was closed
print(my_file.closed)


