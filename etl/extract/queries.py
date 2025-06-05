

etl_query_souerce = {
    'vendedores':{
        'query': '''
            select 
                idVendedor as id_vendedor,
                Vendedor as vendedor,  
                Comision as comision
            from vendedores
        '''
    },
    'clientes':{
        'query': '''
            select 
                c.idCliente as id_cliente,
                c.Cliente as cliente,
                c.CuentaHabilitada as
                cuenta_habilita,
                z.Zona as zona
            from clientes c
                join zonas z 
                    on c.idZona = z.idZona
        '''
    },
    'productos': {
        'query':'''
            select 
                p.idProducto as id_producto,
                p.Producto as producto,
                p.precio as precio,
                r.Rubro as rubro,
                pr.Proveedor as proveedor
            from productos p
                join rubros r 
                    on p.idRubro = r.idRubro
                join proveedores pr
                    on pr.idProveedor = p.idProveedor
            '''
    },
    'ventas':{
        'query':'''
        select 
            c.idCliente  id_cliente,
            p.idProducto id_producto,
            v.idVendedor  id_vendedor,
            cast(max(f.fecha) as date) id_tiempo,
            cast(sum(fd.cantidad * p.precio) as decimal(18,2)) importe_recaudado,
            count(*) as cant_vendida
        from facturacabecera f
            join clientes c
                on c.idCliente = f.idCliente
            join vendedores v
                on v.idVendedor = f.idVendedor
            join facturadetalle fd
                on f.idFactura = fd.idFactura
            join productos p 
                on p.idProducto = fd.idProducto
        group by p.idProducto,c.idCliente,v.idVendedor,f.idFactura
'''
    }
}

etl_query_datawarehouse={
    'vendedores':{
        'query' : '''
            select 
                id_vendedor,
                vendedor
            from l_vendedores
        '''
    },
    'clientes':{
        'query' : '''
            select 
                id_cliente,
                cliente,
                zona
            from l_clientes
        '''
    },
    'productos': {
        'query': '''
            select 
                id_producto,
                producto,
                precio,
                rubro,
                proveedor
            from l_productos
        '''
    },
    'tiempo':{
        'query': '''
            select 
                id_tiempo,
                fecha,
                trimestre,
                mes_anio,
                semana_mes
            from l_tiempo
        '''
    },
    'ventas':{
        'query': '''
            select 
                fv.id_cliente,
                fv.id_producto,
                fv.id_vendedor,
                lt.id_tiempo,
                fv.cant_vendida,
                fv.importe_recaudado
            from f_ventas fv
                join l_tiempo lt 
                    on fv.id_tiempo = lt.id_tiempo
        '''
    }
}