### written by Anthony Erdenetuguldur on 05/13/2022
### the following data capture is used for Clover Take Home Challenge purposes

import pandas as pd
import requests
import os
import os.path
from datetime import datetime, time, date

## host url
## https://api.census.gov/data/2021/pep/population

save_path = '/Users/username/Downloads/'
run_datetime = datetime.today() 

print('run datetime:', datetime.today())

## phase 2 : dev signal failure handler using file creation
## phase 2 : placeholder for database connection / remove prev file

def get_us_pop_census(year):

	HOST = 'https://api.census.gov/data'

	dataset = 'pep/population'

	base_url = '/'.join([HOST, year, dataset])

	predicates = {}

	get_vars = ["GEONAME","POP"]

	predicates["get"] = ",".join(get_vars)

	predicates["for"] = "state:*"

	r = requests.get(base_url, params = predicates)

	# print(r.text)

	col_names = ["state_name", "total_pop",'state_code']

	# create data frame on the api pull
	df = pd.DataFrame(columns=col_names,data=r.json()[1:])

	# add year
	df = df.assign(year = year)

	# fix/ensure correct datatypes
	df['total_pop'] = df['total_pop'].astype(int)
	df['state_code'] = df['state_code'].astype(int)
	df['year'] = df['year'].astype(int)

	return df 

## connect and capture 2016 to 2018 population census 
df_pop16 = get_us_pop_census('2016')
df_pop17 = get_us_pop_census('2017')
df_pop18 = get_us_pop_census('2018')

uspop_frames = [df_pop16, df_pop17, df_pop18]
uspop_result = pd.concat(uspop_frames)

## check top 10 result
print()
print(uspop_result.head(11))

# ## save file for Tableau export
# file_save_time = date.today()
# uspop_result.to_csv(save_path+f'uscensus_2016_to_2018_pop.csv')

# ## use of file_path method to confirm data pull 
# my_file_path = ('/Users/anthonyerdene/Downloads/uscensus_2016_to_2018_pop.csv')
# print('\nIs File/Data Ready for Tableau?', os.path.exists(my_file_path))
# ## check completion
# print('\nprogram completion time:', datetime.now())
