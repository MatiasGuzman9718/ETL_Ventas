import pandas as pd

def extract(engine, query = ''):
    df = pd.read_sql(query, engine)
    return df


def extract_all(engine,dict_queries):
    list_df = []
    for _,value in dict_queries.items():
        df = pd.read_sql(value['query'], engine)
        list_df.append(df)
    return list_df


