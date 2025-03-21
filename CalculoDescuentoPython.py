def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamadas a la función con diferentes parámetros
monto1 = 200
monto2 = 500
porcentaje_personalizado = 30

descuento1 = calcular_descuento(monto1)
descuento2 = calcular_descuento(monto2, porcentaje_personalizado)

print(f"Compra 1: Monto Total = ${monto1}, Descuento Aplicado = ${descuento1}, Monto Final = ${monto1 - descuento1}")
print(f"Compra 2: Monto Total = ${monto2}, Descuento Aplicado = ${descuento2}, Monto Final = ${monto2 - descuento2}")
