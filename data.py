import pandas as pd

df = pd.read_csv('data.csv')
df['GAME_DATE'] = pd.to_datetime(df.GAME_DATE)

def get_columns() -> list:
    return df.columns.tolist()

def get_column_data(column_name: str) -> list:
    return df[column_name].tolist()

def get_column_data_unique(column_name: str) -> list:
    return df[column_name].unique().tolist()
