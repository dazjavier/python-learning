import sys

'''
Contiene array de argumentos:

`python main.py test=01` --> ['main.py', 'test=True']

'''
print(sys.argv)


'''
  Números!
  
  Ref: https://docs.python.org/3/library/stdtypes.html#typesnumeric
'''

print(2 + 2)              # 4
print(50 - 5 * 6)         # 20
print((50 - 5 * 6) / 4)   # 5.0
print(8 / 5)              # 1.6 (Divisiones siempre retornan un `float`)

iva = 0.19
precio_sin_iva = 2990
precio_con_iva = precio_sin_iva + (precio_sin_iva * iva)
print(f"Precio final: {precio_con_iva}")  # Precio final: 3558.1
                                          # Se puede combinar `float` e `int` en operaciones matemáticas


# División
print(6 / 3)    # 2.0
print(18 // 5)  # 3 (Retorna un `int` redondeado hacia abajo)
print(17 % 3)   # 2

# Potencias
print(2 ** 2)  # 4
print(2 ** 7)  # 128


'''
  Variables
'''

width = 40
height = 40

area = width * height
print(area)  # 1600
