x = 0 
while x < 10:
    print("valor de x: " ,str(x))
    x+=1
#juego de puntaje dependiendo el string que ingrese el usuario 

score = 100
x = 0
while x<4:
    shot = input("Ingrese su tiro: " )
    if shot == "hit":
        score+=10
    elif shot == "miss":
        score-=20
    
    x+=1 
print(score)