import pandas as pd

def load_data(engine,list_names,list_df):
    for df,name in zip(list_df, list_names):
        df.to_sql(
            name=name,
            con=engine,
            if_exists='append',
            index=False
        )


def load_data_time(start_time, end_time,engine= ''):
    date_range = pd.period_range(start= start_time, end = end_time, freq = 'D')
    df_l_tiempo = pd.DataFrame({'fecha': date_range})
    df_l_tiempo['fecha'] = df_l_tiempo['fecha'].dt.to_timestamp()
    df_l_tiempo['trimestre'] = df_l_tiempo['fecha'].dt.quarter
    df_l_tiempo['mes_anio'] = df_l_tiempo['fecha'].dt.year * 100 + df_l_tiempo['fecha'].dt.month
    df_l_tiempo['semana_mes'] = ((df_l_tiempo['fecha'].dt.day -1) // 7 + 1)
    df_l_tiempo['id_tiempo'] = df_l_tiempo['fecha'].dt.strftime('%Y%m%d').astype(int)
    df_l_tiempo = df_l_tiempo.reindex(columns=['id_tiempo', 'fecha', 'trimestre', 'mes_anio', 'semana_mes'])
    df_l_tiempo.to_sql(
         name='l_tiempo',
         con=engine,
         if_exists='append',
         index=False
     )

