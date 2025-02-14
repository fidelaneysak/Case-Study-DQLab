## Import Data
    import pandas as pd

    df = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/data_retail.csv', sep=';')  

## Data cleaning and Modification for Further Analysis

  # First_Transaction Column
    df['First_Transaction'] = pd.to_datetime(df['First_Transaction']/1000, unit='s', origin='1970-01-01')
  # Last_Transaction Column
    df['Last_Transaction'] = pd.to_datetime(df['Last_Transaction']/1000, unit='s', origin='1970-01-01')

    print('Lima data teratas:')
    print(df.head())

    print('\nInfo dataset:')
    print(df.info())
