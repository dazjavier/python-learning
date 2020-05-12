import sys

'''
Contiene array de argumentos:

`python main.py test=True` --> ['main.py', 'test=True']

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


'''
  Strings
'''
palabra = 'palabra'
frase = 'Esta es una frase. Aquí se necesitan escapar las single cuotes -> \''

print(palabra)
print(frase)

print('C:\some\name')   #  `\n` es una nueva línea! 😮
print(r'C:\some\name')  # Raw string


mi_palabra = "Python"

print(mi_palabra[0])    # P
print(mi_palabra[5])    # n
print(mi_palabra[-1])   # n
print(mi_palabra[2:4])  # th
print(mi_palabra[:2])   # Py
print(mi_palabra[2:])   # thon


''' 
  Listas (Lists o Arrays)
'''
cubos = [1, 4, 9, 16, 25]

print(cubos[1])   # 4
print(cubos[-1])  # 25
print(cubos[3:])  # [16, 25]

print(cubos + [36, 49, 64, 81, 100])  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(cubos)                          # [1, 4, 9, 16, 25]

print(len(cubos)) # 5


'''
  Fibonacci

  Facílisimo de implementar
'''

a, b = 0, 1

while a < 1000:
  print(a, end=',') # `end=','` reemplaza el valor por default, que es un salto de línea (`\n`)
  a, b = b, a+b