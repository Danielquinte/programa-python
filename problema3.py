#Matriz de inventario
inventario = [
    ["RF001", "Lapiceros", 10, 30],
    ["RF002", "Marcadores", 20, 40],
    ["RF003", "Borradores", 8, 30],
    ["RF004", "Cuadernos", 40, 70],
    ["RF005", "Reglas", 15, 50],
] 

#Modulo: Calcular cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0

#Auditoría y generación de pedidos
def auditar_inventario(inventario):
    print("Inventario:")
    hay_pedidos = False

    for articulo in inventario:
        codigo, nombre, stock_actual, stock_min = articulo
        cantidad = calcular_pedido(stock_actual, stock_min)

        print(f"Stock actual: {stock_actual}")
        print(f"Stock minimo: {stock_min}")

        if cantidad > 0:
            print(f"[{codigo}] {nombre}: Pedir {cantidad} unidades")
            hay_pedidos = True
        else:
            print(f"[{codigo}] {nombre}: Stock suficiente")

auditar_inventario(inventario)

