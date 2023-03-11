#el objetivo del codigo es verificar si el año es biciesto 
year = int(input("Ingrese año: "))
#your code goes here
if year % 4 != 0:
    print("Not a leap year") 
elif year % 100 != 0:
    print("Leap year")
elif year % 400 == 0:
            print("Leap year")
elif year % 400 != 0:
    print("Not a leap year")   
#purificador de oro 
purity = float(input())
#your code goes here
if purity >= 99.9:
    print("24K")
if purity < 99.9 and purity >= 91.7:
    print("22K")
if purity < 91.7 and purity >= 83.3:
    print("20K")
if purity < 83.3:
    print("18K")    
#bucle while 
x = 1
while x < 10:
  if x%2 == 0:
    print(str(x) + " is even")
  else:
    print(str(x) + " is odd")

  x += 1