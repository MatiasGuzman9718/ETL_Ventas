from sqlalchemy import Table, Column, Integer, String,MetaData,Float,ForeignKey,Date
from config.db import engine_staging
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../../')))

os.system('cls ')

metadata_obj = MetaData()

l_productos =Table(
    'l_productos',
    metadata_obj,
    Column('id_producto',Integer,primary_key=True),
    Column('producto',String(100),nullable=False),
    Column('precio',Float,nullable=False),
    Column('rubro',String(100),nullable=False),
    Column('proveedor',String(100),nullable=False)
)

l_clientes = Table(
    'l_clientes',
    metadata_obj,
    Column('id_cliente',Integer,primary_key=True,nullable=False),
    Column('cliente',String(100),nullable=False),
    Column('zona',String(100),nullable=False)
)

l_vendedores = Table(
    'l_vendedores',
    metadata_obj,
    Column('id_vendedor',Integer,primary_key=True),
    Column('vendedor',String(100),nullable=False),
)

l_tiempo = Table(
    'l_tiempo',
    metadata_obj,
    Column('id_tiempo',Integer,primary_key=True),
    Column('fecha',Date,nullable=False),
    Column('trimestre',Integer,nullable=False),
    Column('mes_anio',Integer,nullable=False),
    Column('semana_mes',Integer,nullable=False)
)

f_ventas = Table(
    'f_ventas',
    metadata_obj,
    Column('id',Integer,primary_key=True,autoincrement=True),
    Column('id_cliente',Integer,ForeignKey('l_clientes.id_cliente'),nullable=False),
    Column('id_producto',Integer,ForeignKey('l_productos.id_producto'),nullable=False),
    Column('id_vendedor',Integer,ForeignKey('l_vendedores.id_vendedor'),nullable=False),
    Column('id_tiempo',Integer,nullable=False),
    Column('cant_vendida',Float,nullable=False),
    Column('importe_recaudado',Float,nullable=False)
)

metadata_obj.create_all(engine_staging)