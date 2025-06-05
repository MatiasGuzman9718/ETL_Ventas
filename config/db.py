from sqlalchemy import create_engine,text
import configparser
import os

os.system('cls')
path  = 'D:\ESCRITORIO\etl_practica\config'
config = configparser.ConfigParser()
config.read(os.path.join(path,'config.ini'))
db_config = config['origen']

def conection_db(config,name_conn):
    name_conn = create_engine(f'mysql+pymysql://{config["user"]}:{config["password"]}@{config["host"]}:{config["port"]}/{config["database"]}')
    return name_conn

# Conexión a origen
engine_origen = conection_db(config['origen'],'engine_origen')

#Conexión a staging
engine_staging = conection_db(config['staging'],'engine_staging')   

# Conexión a datawarehouse
engine_datawarehouse = conection_db(config['datawarehouse'],'engine_datawarehouse')

try: 
     with engine_origen.connect() as conn:
         result= conn.execute(text("SELECT 1"))
         print(result.fetchone())
        
except Exception as e:
     print(f"Error al conectar a la base de datos de staging: {e}")