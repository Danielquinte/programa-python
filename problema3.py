#Inventario
inventario = [
    ["A001", "Teclado USB", 8, 15],
    ["A002", "Mouse Inalámbrico", 20, 10],
    ["A003", "Monitor 24 pulgadas", 3, 5],
    ["A004", "Silla Ergonómica", 12, 12],
    ["A005", "Auriculares Bluetooth",1, 8],
]

#Módulo: Calcular cantidad a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    return 0

#Auditoría y generación de pedidos
def auditar_inventario(inventario):
    print("═══ LISTA DE PEDIDOS ═══")
    hay_pedidos = False

    for articulo in inventario:
        codigo, nombre, stock_actual, stock_min = articulo
        cantidad = calcular_pedido(stock_actual, stock_min)

        print(f"Stock actual: {stock_actual}")
        print(f"Stock minimo: {stock_min}")

        if cantidad > 0:
            print(f"[{codigo}] {nombre}: PEDIR {cantidad} unidades")
            hay_pedidos = True
        else:
            print(f"[{codigo}] {nombre}: Stock suficiente")

    if not hay_pedidos:
        print("Todo el inventario está al día.") 

#print(f"{cantidad}") 

auditar_inventario(inventario)

