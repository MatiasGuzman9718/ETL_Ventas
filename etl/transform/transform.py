import pandas as pd
import os 

os.system('cls')

def drop_dupli(dataframe):
    df = dataframe.drop_duplicates()
    return df

def rename_columns(df,colums):
    current_names = df.columns
    for on , nm in zip(current_names, colums): # on = old name, nm = new name
        df.rename(columns={on: nm}, inplace=True)
    return df

def transform_date(df,columns):
    for col in columns:
        df[col] = pd.to_datetime(df[col]).dt.strftime('%Y%m%d').astype(int)
    return df

def reindex_columns(df,columns):
    df = df.reindex(columns=columns)
    return df