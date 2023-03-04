# if condicion:
#    codigo, al principio de la linea esta indentado 
x = input("Ingrese un numero: ") 
if int(x) > 5: #para comparar una entrada por teclado primero se tiene que pasar a int o float 
    print(int(x), "es mayor que 5")
else:
    print(int(x), "es menor que 5")