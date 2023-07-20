import pandas as pd

data = pd.read_excel('data-raw/gov_emissions.xlsx', sheet_name="Passenger vehicles", skiprows=24, nrows=20, engine='openpyxl')
print(data)