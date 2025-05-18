# Lista de ventas (datos de ejemplo)
ventas = [
    {"fecha": "2024-01-01", "producto": "Camisa", "cantidad": 5, "precio": 25.54},
    {"fecha": "2024-01-01", "producto": "Pantalón", "cantidad": 3, "precio": 39.49},
    {"fecha": "2024-01-02", "producto": "Camisa", "cantidad": 2, "precio": 27.49},
    {"fecha": "2024-01-02", "producto": "Zapatos", "cantidad": 1, "precio": 80.55},
    {"fecha": "2024-01-03", "producto": "Pantalón", "cantidad": 4, "precio": 35.89},
    {"fecha": "2024-01-03", "producto": "Zapatos", "cantidad": 2, "precio": 85.50},
    {"fecha": "2024-01-04", "producto": "Camisa", "cantidad": 3, "precio": 30.56},
    {"fecha": "2024-01-04", "producto": "Sombrero", "cantidad": 1, "precio": 20.78},
]

# 1. Cálculo de Ingresos Totales
ingresos_totales = 0
for venta in ventas:
    ingresos_totales += venta["cantidad"] * venta["precio"]

print(f"\n1. Ingresos totales: ${ingresos_totales:.2f}")

# 2. Análisis del Producto Más Vendido
ventas_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    if producto in ventas_por_producto:
        ventas_por_producto[producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print(f"\n2. Producto más vendido: {producto_mas_vendido} (Cantidad: {ventas_por_producto[producto_mas_vendido]})")

# 3. Promedio de Precio por Producto
precios_por_producto = {}
for venta in ventas:
    producto = venta["producto"]
    cantidad = venta["cantidad"]
    precio = venta["precio"]
    
    if producto in precios_por_producto:
        suma_precios, total_unidades = precios_por_producto[producto]
        precios_por_producto[producto] = (suma_precios + precio * cantidad, total_unidades + cantidad)
    else:
        precios_por_producto[producto] = (precio * cantidad, cantidad)

print("\n3. Precio promedio por producto:")
for producto, (suma_precios, total_unidades) in precios_por_producto.items():
    promedio = suma_precios / total_unidades
    print(f"- {producto}: ${promedio:.2f}")

# 4. Ventas por Día
ingresos_por_dia = {}
for venta in ventas:
    fecha = venta["fecha"]
    ingreso = venta["cantidad"] * venta["precio"]
    
    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

print("\n4. Ingresos por día:")
for fecha, ingreso in ingresos_por_dia.items():
    print(f"- {fecha}: ${ingreso:.2f}")

# 5. Resumen de Ventas por Producto
resumen_ventas = {}
for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]
    suma_precios, total_unidades = precios_por_producto[producto]
    ingresos_totales_producto = suma_precios
    precio_promedio = suma_precios / total_unidades
    
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos_totales_producto,
        "precio_promedio": precio_promedio
    }

print("\n5. Resumen de ventas por producto:")
for producto, datos in resumen_ventas.items():
    print(f"\nProducto: {producto}")
    print(f"- Cantidad total vendida: {datos['cantidad_total']}")
    print(f"- Ingresos totales: ${datos['ingresos_totales']:.2f}")
    print(f"- Precio promedio: ${datos['precio_promedio']:.2f}")