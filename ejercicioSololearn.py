#el objetivo del codigo es verificar si el año es biciesto 
year = int(input("Ingrese año: 1966"))
#your code goes here
if year % 4 != 0:
    print("Not a leap year") 
elif year % 100 != 0:
    print("Leap year")
elif year % 400 == 0:
            print("Leap year")
elif year % 400 != 0:
    print("Not a leap year")   