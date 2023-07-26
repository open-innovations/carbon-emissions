import pandas as pd
import os
from openpyxl import load_workbook

DATA_DIR = "data/"

def read_data(**args):
    #unpack args.
    filepath = args['filepath']
    sheet_name = args['sheet_name']
    skiprows = args['skiprows']
    nrows = args['nrows']
    engine = args['engine']
    data = pd.read_excel(filepath, sheet_name=sheet_name, skiprows=skiprows, nrows=nrows, engine=engine)

    #remove repeat colum headings
    data = data[data.Activity != "Activity"]
    return data

def comments_to_csv(data, filepath, sheet_name):
    #only take filled cells
    info = data[data.Type.notnull()]
    #load the data
    workbook = load_workbook(filepath)
    worksheet = workbook[sheet_name]
    #create empty list
    description = []

    #get the comment for each relevant cell in the "type" column.
    for row in worksheet.iter_rows(min_col=1, max_col=2):
        for cell in row:
            if cell.comment:
                comm = cell.comment.text
                arr = comm.split("Comment:")
                description.append(arr[1])

    transport_type = info.Type.to_list()
    assert len(transport_type) ==  len(description)
    
    info = dict()
    for i, j in zip(transport_type, description):
        info.update({i:j})

    info_as_frame = pd.Series(data=info, name='Description')
    info_as_frame = info_as_frame.replace("\n", "")
    info_as_frame = info_as_frame.str.strip()
    info_as_frame.to_csv(os.path.join(DATA_DIR, 'transport_type_info.csv'))
    return info_as_frame

if __name__ == "__main__":
    data = read_data(filepath='data-raw/gov_emissions.xlsx', sheet_name="Passenger vehicles", skiprows=24, nrows=43, engine="openpyxl")
    transformed_data = data.loc[:, ["Activity", "Type", "Unit", "kg CO2e", "kg CO2e.1", "kg CO2e.2", "kg CO2e.3"]]
    transformed_data.rename(columns={"kg CO2e": "Diesel", "kg CO2e.1": "Petrol", "kg CO2e.2": "Unknown", "kg CO2e.3": "Plugin hybrid electric vehicle"}, inplace=True)
    transformed_data.to_csv(os.path.join(DATA_DIR, 'transformed_carbon_emissions.csv'))
    
    comments_to_csv(data, filepath='data-raw/gov_emissions.xlsx', sheet_name="Passenger vehicles")