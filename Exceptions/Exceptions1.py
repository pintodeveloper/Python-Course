def sum(n1,n2):
    return n1+n2

def mul(n1,n2):
     return n1*n2

def div(n1,n2):
    try:
        return n1/n2
    except:
        print("No se puede dividir por 0")
        return "Operacion erronea"

def res(n1,n2):
    return n1-n2

message= "si deseas realizar una operacion escribe: suma, resta, divide, multiplica"

print(message)

operations = input()
result = ""
errorOperation = False

while(True):
    try:
        n1 = int(input("Ingrese el primer #: "))
        n2 = int(input("Ingrese el segundo #: "))
        break
    except ValueError:
        print("Los datos ingresados no son numericos.")

if(operations.lower() =="suma"):
    result = sum(n1,n2)
elif(operations.lower() =="resta"):
    result = res(n1,n2)
elif(operations.lower() =="divide"):
    result = div(n1,n2)
elif(operations.lower() == "multiplica"):
    result = mul(n1,n2)
else:
    errorOperation = True

if(errorOperation):
    print("Operacion no contemplada")
else:
    print("El resultado es ",result)
    print("operacion ejecutada. continua proceso...")