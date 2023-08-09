import pandas as pd
import os

PATH = "data-raw/emission_factors_flat_file.xlsx"

def read_data(**args):
    # unpack args.
    filepath = args['filepath']
    sheet_name = args['sheet_name']
    skiprows = args['skiprows']
    nrows = args['nrows']
    engine = args['engine']

    # read the file
    data = pd.read_excel(filepath, sheet_name=sheet_name, skiprows=skiprows, nrows=nrows, engine=engine)

    return data

def transform(data):
    # only get the data we are interested in
    types = ['Passenger vehicles', 'Business travel- air', 'Business travel- sea', 'Business travel- land']
    data = data[data['Level 1'].isin(types)]

    # only use ttotal co2 equivalent factors
    data = data[data['GHG/Unit'] == 'kg CO2e']

    # drop duplicate rows
    data.drop(data[(data['Level 1'] == 'Business travel- land') & ((data['Level 2'] == 'Cars (by market segment)') | (data['Level 2'] == 'Cars (by size)'))].index, inplace=True)
    data.drop(columns='Level 1', inplace=True)

    # extract "column text" into two separate columns as it contains different types of data
    # remove the old data from the original column
    data['return_flight'] = data['Column Text'].str.extract('(With RF|Without RF)', expand=True)
    data['Column Text'] = data['Column Text'].str.replace('(With RF|Without RF)', '', regex=True)
    
    data['variable_name'] = 'GHG Conversion Factor 2023'

    # rename columns
    renames = {'UOM': 'distance_unit', 'Level 2': 'activity', 'Level 3': 'type', 'Level 4': 'flight_class', 'GHG/Unit': 'ghg_unit', 'GHG Conversion Factor 2023':'value', 'Column Text': 'fuel_type'}
    data.rename(columns=renames, inplace=True)

    # re-order columns
    data = data.reindex(columns=['Scope', 'activity', 'type', 'fuel_type', 'flight_class', 'return_flight', 'ghg_unit', 'distance_unit', 'variable_name', 'value']).set_index('Scope')
    return data

if __name__ == "__main__":
    
    # read the data in and transform it
    data = read_data(filepath=PATH, sheet_name="Factors by Category", skiprows=5, nrows=8039, engine="openpyxl")
    data = transform(data)
    
    # write to file
    data.to_csv('data/emission_factors.csv')

