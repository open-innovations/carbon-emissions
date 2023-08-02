import pandas as pd
import os

DATA_DIR = 'data/transformed/'
OUTDIR = 'data/prepped/'
os.makedirs(OUTDIR, exist_ok=True)

air = pd.read_csv(f'{DATA_DIR}/air_travel.csv')
buses = pd.read_csv(f'{DATA_DIR}/buses.csv')
cars_market_segment = pd.read_csv(f'{DATA_DIR}/cars_market_segment.csv')
cars_size = pd.read_csv(f'{DATA_DIR}/cars_size.csv')
motorbikes = pd.read_csv(f'{DATA_DIR}/motorbikes.csv')
sea_travel = pd.read_csv(f'{DATA_DIR}/sea_travel.csv')
taxis = pd.read_csv(f'{DATA_DIR}/taxis.csv')
trains = pd.read_csv(f'{DATA_DIR}/trains.csv')

frame = pd.concat(
    [
    air,
    buses,
    cars_market_segment,
    cars_size,
    motorbikes,
    sea_travel,
    trains],
    axis=0)
frame.drop(columns="Unnamed: 0", inplace=True)
frame.to_csv(os.path.join(OUTDIR, 'emission_factor_catalogue.csv'))