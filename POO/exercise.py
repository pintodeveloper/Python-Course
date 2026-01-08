"""
Python tutorizado. Ejercicio creación de clases e instancias
Se trata de crear una clase que construya cuentas corrientes bancarias. Para ello deberás:

Crear una clase con el nombre de CuentaCorriente con tres atributos que serán:
El nº de la cuenta (un string numérico con el nº de cifras que quieras)
El titular de la cuenta
El saldo de la cuenta

Crear un método getter que nos muestre la información de la cuenta. 
Debe mostrarnos el nº, el titular y el saldo.
Crear un método que nos permita ingresar dinero en la cuenta
Crear un método que nos permita retirar dinero de la cuenta
 

Prueba el programa creando un objeto de tipo CuentaCorriente, ingresa y retira dinero de la cuenta y finalmente muestra los datos de la
"""

class CountCorriente:
    numberCount = ""
    titular = ""
    saldo = 0

    def __init__(self,numberCount,titular,saldo):
        self.numberCount = numberCount
        self.titular = titular
        self.saldo = saldo


    def getDates(self):
        return "El nº del titular de la cuenta es "+self.numberCount+ \
        " su nombre es "+self.titular + " su saldo es de: "+str(self.saldo)

    def enterMoney(self,money):
        self.saldo += money

    def returnMoney(self,money):
        self.saldo -= money 

    def showSaldo(self):
        return "El saldo de "+self.titular+" es de: "+str(self.saldo)


p1 = CountCorriente("545677","Pinto 77",777000000)

print("####################################")

print(p1.getDates())

p1.enterMoney(0)

print(p1.showSaldo())

p1.returnMoney(7000000)

print(p1.showSaldo())

