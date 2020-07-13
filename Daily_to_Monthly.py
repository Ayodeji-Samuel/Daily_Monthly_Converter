import pandas as pd
import numpy as np


def daily_month(input, output):
    df = pd.read_csv(input)

    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year

    # Check to see if the column to aggregate is in float, if not convert to float
    df['Discharge'] = pd.to_numeric(df['Discharge (m3/s)'], errors='coerce')
    #df['Another_one'] = pd.to_numeric(df['Another_one'], errors='coerce')

    # Add all the columns that are not necessary inside the drop labels list
    df_new = df.drop(labels=['Date', 'Waterlevel', 'Discharge (m3/s)'], axis=1)

    # Apply the mean aggregate
    month_average = df_new.groupby(['Year', 'Month']).mean()

    # Save file in a new .csv file
    month_average.to_csv(output)


input = 'TPC.csv'
output = 'daily_monthly.csv'

daily_month(input, output)
