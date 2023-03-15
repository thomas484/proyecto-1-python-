#ejemplos de listas con ejercicios 
# las lista son usadas para almacenar valores o ítems 
# se crean usando corchetes y comas para separar cada miembro 
dias =["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
i=0
while i < 7:
    print("Hoy es: ", dias[i])
    i+=1
#ejemplo de como se hace una matriz 
m = [
    [1, 2, 3],
    [4, 5, 6]
    ]
    
print(m[1][2]) #se indexa desde el 0, por eso la fila 1 es la segunda y l columna 2 es la última 01, 012
#operador in 
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words) # span está en la lista words ? -> si o True 
print("egg" in words)
print("tomato" in words)
#operador NOT 
nums = [1, 2, 3]
print(not 4 in nums) # 4 está en nums ? -> no -> not -> True
print(4 not in nums) 
print(not 3 in nums) # 3 está en nums ? -> si -> not -> False
print(3 not in nums) 