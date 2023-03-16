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
print(squares[2:6]) #slice  (corte)
print(squares[3:8])
print(squares[0:1])
print(squares[:7]) #si el primer elemento se omite entonces comienza desde el principio (del 0 al 6)
print(squares[7:]) #si el segundo argumento del slice se omite corta hasta el final 
print(squares[::2]) #desde el principo hasta el final, imprime el primer elemento y va de dos en dos 
print(squares[2:8:3])
print(squares[1:-1])# hace un recorrido en bucle sobre la lista, imprime [1,4,9,16,25,36,49,64]
#invierte un string 
#your code goes here
palabra = str(input())
print(palabra[::-1]) 
