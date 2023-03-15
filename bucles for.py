#bucles for 
palabras = ["Hola", "Adiós", "Mundo"]
for f in palabras: #para f en palabras copia y agrega un !
    print(f + "!")
# ejemplo de recorrer un string 
cuenta = 0
palabra = str(input("Ingrese un string: "))
l = str(input("Ingrese el caracter a buscar: "))
for c in palabra:
    if c == l:
        cuenta+=1
print("Coincidencias con la letra a: ", int(cuenta)) 
