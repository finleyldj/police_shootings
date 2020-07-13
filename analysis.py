import pandas as pd
import re
import numpy as np
shootings = pd.read_csv('fatal-police-shootings-data.csv')

#setting up dataframes of US census data for 2015
white = pd.read_csv('ACSDT1Y2015.B01001A_data_with_overlays_2020-07-12T121155.csv')
white = white.transpose()
black = pd.read_csv('ACSDT1Y2015.B01001B_data_with_overlays_2020-07-12T121405.csv')
black = black.transpose()
american_indian = pd.read_csv('ACSDT1Y2015.B01001C_data_with_overlays_2020-07-12T121405.csv')
american_indian = american_indian.transpose()
asian = pd.read_csv('ACSDT1Y2015.B01001D_data_with_overlays_2020-07-12T121405.csv')
asian = asian.transpose()
pacific = pd.read_csv('ACSDT1Y2015.B01001E_data_with_overlays_2020-07-12T121405.csv')
pacific = pacific.transpose()
hispanic = pd.read_csv('ACSDT1Y2015.B01001I_data_with_overlays_2020-07-12T121405.csv')
hispanic = hispanic.transpose()
other = pd.read_csv('ACSDT1Y2015.B01001F_data_with_overlays_2020-07-12T121405.csv')
other = other.transpose()
frames = [white,black,american_indian,asian,pacific,hispanic,other]
#renaming columns for readability
for i in frames:
    i.columns = ['id','number']


#creating a native dataset, as shooting dataset does not account for what type of native someone is
native = american_indian.merge(pacific, how = 'inner', on = 'id', suffixes = ('_A','_P'))
native[['number_A','number_P']] = native[['number_A','number_P']].apply(pd.to_numeric, errors='coerce')
native['number'] = native.number_A + native.number_P
native = native.drop(['number_A', 'number_P'],axis=1)
frames.append(native)
frames.pop(2)
frames.pop(4)

#combining all racial dataframes into one
sufs = ['W','B','A','H','O','N']
census = white.merge(black, how = 'inner', on = 'id', suffixes = ('W,', 'B'))
for i in range(2,len(frames)):
    census = census.merge(frames[i],how='inner', on='id', suffixes = (sufs[i-1],sufs[i]))
census.columns = ['id','W','B','A','H','O','N']
census[sufs] = census[sufs].apply(pd.to_numeric, errors = 'coerce')
census['id']= census['id'].apply(lambda x: x.split('Total!!')[-1])
census['age'] = census['id'].apply(lambda x: x.split('!!')[-1])
census['gender'] = census['id'].apply(lambda x: x.split('!!')[0])
census.drop('id', axis = 1, inplace = True)
census.drop(census.index[0:6], inplace=True)

#creating a dataframe for totals, and a dataframe for margins of error
odd_indexes = list(range(1,59,2)) #these numbers are dodgy
even_indexes = list(range(0,58,2)) #so are these

census_totals = census.iloc[even_indexes]
census_errors = census.iloc[odd_indexes]

#Next up, create pivot table for each. Gender --> M/F/O

#initial exploration of shooting data

#examine trends over time, geography, gender, and race + visualisations

#statistical tests to support conclusions - is the police racist?
