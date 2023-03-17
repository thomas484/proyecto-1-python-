#funciones en python 
# fuciones que se usan en listas 
letras = ["a", "b", "n", "s", "r", "h"]
nums = [1,2,3]
#funcion len
print(letras)
print("Longitud de la cadena:",len(letras))
#funcion append
nums.append(5) #agrega al final de la lista el 5
print(nums) #imprime esto [1,2,3,5]
#funcion insert 
letras.insert(2, "j")
print(letras)
#funcion index
print("Posición de la coincidencia:",letras.index("h")) #si encuentra el mismo caracter devuelve la posición de la coincidencia 
#funcion max(list) devuelve el valor mas alto de la lista 
#fucion min(list) devuelve el valor mas pequeño de la lista 
# list.count(item) busca cuantas veces se repite un ítem de la lista
# list.remove(item) elimina de la lista el item introducido en la funcion 
# list.reverse() invierte los items de la lista 