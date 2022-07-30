# import pandas as pd

# ### Creating a DataFrame using Dictionary 
# ttt_dict = {
# 	'col1' : ['1','4','7'],
# 	'col2' : ['2','5','8'],
# 	'col3' : ['3','6','9'],
# }

# ttt_df = pd.DataFrame(ttt_dict)

# print(ttt_df)


# ### Creating a dictionary using .csv file via the read_csv method
# # data_source = pd.read_csv('/Users/anthonyerdene/Documents/personal_data/sw_ds_de_dev/python_dev/test_files/nba_players.csv')
# # print(data_source)

# # print third column position 1, using column label and index e.g
# print('first value of column 1 is:', ttt_df['col1'][0])


# # print value 9 using iloc method only



# print('last value of col3 is',ttt_df.iloc[2, 2])



# Creating a Dictionary 
Dict = {1: 'Apple', 'name': 'For', 3: 'Banana'}
  
# accessing a element using get()
# method
print("Accessing a element using get:")
print(Dict.get(3))