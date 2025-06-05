import os 
from config.db import engine_origen,engine_staging,engine_datawarehouse
from etl.transform.transform import transform_date,reindex_columns
from etl.load_data.load_data import load_data,load_data_time
from etl.extract.queries import etl_query_souerce,etl_query_datawarehouse
from etl.extract.extract import extract_all

os.system('cls')

def main():
    # Extract data from source
    list_df = extract_all(engine_origen,etl_query_souerce)
    # Process data
    df_vendedor = reindex_columns(list_df[0],['id_vendedor','vendedor'])
    df_cliente = reindex_columns(list_df[1],['id_cliente','cliente','zona'])
    df_producto = list_df[2]
    df_ventas = transform_date(list_df[3],['id_tiempo'])

    list_df_processed = [df_vendedor, df_cliente, df_producto, df_ventas]
    # Load data into staging area
    load_data(engine_staging,
            ['l_vendedores','l_clientes','l_productos','f_ventas'],list_df_processed)
    load_data_time('2008-01-01', '2010-12-31', engine_staging)

    # Extract data from staging area
    list_df_dw = extract_all(engine_staging,etl_query_datawarehouse)
    #Load data into datawarehouse
    load_data(engine_datawarehouse,
            ['l_vendedores','l_clientes','l_productos','l_tiempo','f_ventas'],list_df_dw)

if __name__ == '__main__':
    main()