import random
"""
Cuando el usuario averigüe finalmente el número aleatorio, 
el programa imprimirá en consola “Correcto. 
Has utilizado…” y el nº de intentos consumidos
"""

numberRandom = random.randint(1,100)

number = int(input("Ingrese un numero del 1 al 100 para adivinar: ")) 
countIntent = 1

while(number != numberRandom):
    
    while(number < 0):
        number = int(input("fue negativo no valido, Ingrese un numero del 1 al 100 para adivinar el: ")) 
        
    if(number > numberRandom):
        print("El numero ingresado es mayor al numero que estas adivinando!")
    else:
        print("El numero ingresado es menor al numero que estas adivinando!")
    
    countIntent += 1
    number = int(input("Ingrese un numero del 1 al 100: ")) 
    
    
print("Correto! has utilizado ",countIntent," Intentos consumidos" )