# if condicion:
#    codigo, al principio de la linea esta indentado 
import math 
import cmath 

x = input("Ingrese un numero: ") 
if int(x) > 5: #para comparar una entrada por teclado primero se tiene que pasar a int o float 
    print(int(x), "es mayor56 que 5")
else:
    print(int(x), "es menor que 5")
#conversor de temp.
fahrenheit = input("Ingrese la temperatura en grados Fahrenheit: ") #para que no entre dentro del else debe ir un espacio antes 
celcius = (float(fahrenheit) - 32) * 5/9
print("En Celcius: ", celcius)
#usando la libreria math
print(math.pi)
#usando la libreria math para numeros complejos cmath 
number = complex(4,5) #creo un numero complejo   
print(cmath.phase(number), "rad") #imprime la fase del numero en radianes 
print(float(19/46))