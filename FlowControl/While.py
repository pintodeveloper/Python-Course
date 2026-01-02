count = 0

while count < 10:
    print(77)
    count+=1
    
#print("Hemos salido del bucle")



age = int(input("Introduce tu edad, por favor: "))

while age < 0 or age > 150:
    print("has introducido una edad negativa no es valida ")
    age = int(input("introduce tu edad, por favor: "))

print("Gracias puedes pasar:")
print("Edad del usuario es de " + str(age))