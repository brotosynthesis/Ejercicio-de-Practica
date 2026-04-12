usuario="Pepe"
item1="Postal 2 Redux OST CD"
item2="Silent Hill F OST CD"
item3="Almohada Nekopara Vanilla 30x20"
precios=[40000, 50000, 30000]

def listar_productos(p1, p2, p3):
    print("Carrito de Compras")
    carrito=[p1, p2, p3]
    for i, producto in enumerate(carrito, 1):
        print(f"{i}. {producto}")
    return len(carrito)

def calc_descuento(precio_base, edad_cliente, miembro):
    descuento=0
    if edad_cliente < 18:
        descuento += 10
    if miembro:
        descuento += 15
    precio_final=precio_base-(precio_base*(descuento/100))
    return precio_final

def factura(nombre, total, ubicacion, categoria, total_items, contador):
    impuesto=0.21
    total_impuesto=total*(1+impuesto)
    print("Factura:")
    print("Cliente:", nombre)
    print("Región de envío:", ubicacion)
    print("Categoría del cliente: ", categoria)
    print("Cantidad de productos:", total_items)
    print("Intentos realizados:", contador)
    print("Subtotal con descuentos: $", total)
    print("El total a pagar es de: $", total_impuesto)
    print("¡Muchas gracias por su compraa!")


def clasificar_cliente(edad, total, miembro):
    if edad<18:
        return "Cliente menor"
    elif miembro:
        return "Cliente vip"
    else:
        return "Cliente regular"

def calc_total_producs(precios, extra1, extra2):
    suma=0
    for precio in precios:
        suma+=precio
    return suma

def contar_intentos(max_intentos, numero_objetivo, inicio):
    contador=inicio
    while contador<max_intentos:
        contador+=1
    return contador

cantidad=listar_productos(item1, item2, item3)
total_productos=calc_total_producs(precios, 0, 0)
precio_desc=calc_descuento(total_productos, 20, True)
categoria_cliente=clasificar_cliente(20, total_productos, True)
intentos=contar_intentos(3, 0, 0)

factura(usuario, precio_desc, "Jujuy", categoria_cliente, cantidad, intentos)