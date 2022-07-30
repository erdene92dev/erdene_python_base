# It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is properly closed 
# after its suite finishes, even if an exception is raised at some point. 
# Using with is also much shorter than writing equivalent try-finally blocks:
import csv

with open("/Users/anthonyerden/Documents/sw-ds-development/python_dev/files/example_transactions.csv") as t:
	read_data = t.read()
	print(t)
	# print(read_data)

t.closed


# with open('/Users/anthonyerden/Documents/sw-ds-development/python_dev/files/nba_players.csv', 'w', newline='\n') as file:
# 	field_names = ['player', 'nba_rating']
# 	writer = csv.DictWriter(file, fieldnames=field_names)

# 	writer.writeheader()
# 	writer.writerow({'player':'Michael Jordan', 'nba_rating':99}), 
# 	writer.writerow({'player':'Allen Iverson', 'nba_rating':89}),
# 	writer.writerow({'player':'Magic Johnson', 'nba_rating':90})

