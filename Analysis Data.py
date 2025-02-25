## Classification Customer

  # Checking the last transaction in the dataset
    print(max(df['Last_Transaction']))

  # Classify customers who are churn or not
    df.loc[df['Last_Transaction'] <= '2018-08-01', 'is_churn'] = True 
    df.loc[df['Last_Transaction'] > '2018-08-01', 'is_churn'] = False 

## Delete columns that are not needed
    del df['no']
    del df['Row_Num']
