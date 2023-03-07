# if condicion:
#    codigo, al principio de la linea esta indentado 
import math 
x = input("Ingrese un numero: ") 
if int(x) > 5: #para comparar una entrada por teclado primero se tiene que pasar a int o float 
    print(int(x), "es mayor que 5")
else:
    print(int(x), "es menor que 5")

fahrenheit = input("Ingrese la temperatura en grados Fahrenheit: ") #para que no entre dentro del else debe ir un espacio antes 
celcius = (float(fahrenheit) - 32) * 5/9
print("En Celcius: ", celcius)
print(math.pi)