#funcion range()
numeros = list(range(10))
for i in numeros:
 print(str(numeros[i]) + "!") # imprime los números del 0 al 11, range genera numeros en la forma de dato lista
#0!
#1! 
#2! ...
#9!
#argumentos en la funcion range(inicio,fin,step)
conjuntoenpasos = list(range(1,10,2)) # [inicio, fin, step)
conjunto = list(range(1,10)) # [inicio, fin)
print(conjunto)
print(conjuntoenpasos)
#imprime tramos de la lista 
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
