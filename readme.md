**Proyecto ETL Ventas**<br>
    Se busca dar respuesta a los siguients requisitos de información:<br>
        1) Cantidad de unidades vendidas de cada producto considerando al cliente, vendedor y la fecha.<br>
        2) Suma total recaudad por producto considerando al cliente, vendedor y la fecha.<br>
    Como los indicadores con los que se esta trabajando y teniendo en consideración lo establecido en la metodología **Hefesto** se reunen los indicadores en una sola tabla de hechos.<br>

**Flujo de Trabajo**<br>

        1)Extracción<br>
    Los datos son extraídos de una base de datos **MYSQL** utilizzando una conexión establecida mediante las librerias SQLAlchemy y Pandas.
    
        2)Transformación 
    Durante este etapa. los datos extraidos son limpiados , reestructurados y filtrados con el fin de que los datos sean cargados en el datawarehouse sean de calidad y sirvan para dar respuestas a los requisistos planteados al principio del proyecto.

    Además, se definieron explícitamente los esquemas de la base de datos staging y del datawarehouse utilizando SQLAlkchemy Core.
    
        3)Carga
    Una vez transformados y validados los datos se realizo la carga de los datos al datawarehouse utilizando las librerias antes mencionadas.

