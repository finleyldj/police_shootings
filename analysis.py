import pandas as pd
shootings = pd.read_csv('fatal-police-shootings-data.csv')

#setting up dataframes of populations by race
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

for i in frames:
    i.columns = ['id','number']


#creating a dataframe for natives
natives = american_indian.merge(pacific, how = 'inner', on = 'id', suffixes = ('_A','_P'))
natives[['number_A','number_P']] = natives[['number_A','number_P']].apply(pd.to_numeric, errors='coerce')
natives['number'] = natives.number_A + natives.number_P
frames.append(natives)
frames.pop(2)
frames.pop(4)

#combining all racial dataframes into one
#ttt
#for i in range(len(frames)):


#initial exploration of shooting data

#examine trends over time, geography, gender, and race

#statistical tests to support conclusions
