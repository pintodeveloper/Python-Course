import math

def calculateSquare(number):
    if number < 0:
        #La palabra reservada raise, sirve para obligar a otros programadores a utilizar un try: except:
        raise ValueError ("El # no puede ser negativo")
    else:
        return math.sqrt(number)

numberUser = int(input("Ingresa un #: "))

try:
    print(calculateSquare(numberUser))
except ValueError:
    print("Erro de # negativo.. ")
    
print("Y por aqui continuaria el programa...")