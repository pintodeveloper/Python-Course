"""
Se trata de crear una clase con el nombre CuentaJoven que construya cuentas corrientes bancarias 
heredando de la clase CuentaCorriente creada en el ejercicio del vídeo 33. Puedes crear la clase 
en el mismo fichero del ejercicio 33 (a continuación de la clase CuentaCorriente) o en un fichero aparte.

La clase CuentaJoven tendrá un atributo o propiedad propia con el nombre de bonus_promocion. 
El atributo bonus_promocion permitirá, de forma opcional,
añadir un bonus que se añadirá al saldo de la cuenta.
 
- El establecimiento del bonus y el incremento del saldo se harán desde el constructor.

Además, la clase CuentaJoven contará con los siguientes métodos:

getBonus() encargado de devolver el importe del bonus
ingresar() que permitirá ingresar dinero a la cuenta. Este método se heredará de CuentaCorriente
retirar() que permitirá retirar dinero de la cuenta. Este método se heredará de CuentaCorriente

getDatos() que permitirá ver los datos de la Cuenta Joven: nº de cuenta, titular, saldo y bonus. 
Este método se heredará de CuentaCorriente
Prueba el programa creando un objeto de tipo CuentaJoven, ingresa y retira dinero de la cuenta y finalmente muestra los datos de la cuenta.

Ejercicio y Solución en PDF
"""

class CurrentAccount():
    
    def __init__(self,numberCount,holder,totalMoney):
        self.numberCount = numberCount
        self.holder = holder
        self.totalMoney = totalMoney

    def getDates(self):
        return "#Cuenta: "+ str(self.numberCount) + " Titular: "+self.holder+" Total de dinero: "+ str(self.totalMoney)

    def inputMoney(self,money):
        self.totalMoney += money
        
    def withdrawMoney(self,money):
        self.totalMoney -= money 
        

class CountYoung(CurrentAccount):
    
    def __init__(self,numberCount,holder,totalMoney,bonusPromotion):
        super().__init__(numberCount,holder,totalMoney)
        
        self.bonusPromotion= bonusPromotion

    def getBous(self):
        return "El total del bonus es de : "+str(self.bonusPromotion)
    
    def inputMoney(self,money):
        super().inputMoney(money)

    def withdrawMoney(self,money):
        super().withdrawMoney(money)

    def getDates(self):
        return super().getDates() + " Bonus "+str(self.bonusPromotion)

countYoung1 = CountYoung(4555588,"Pinto77",77008000000,77000000)

countYoung1.withdrawMoney(2000000)
countYoung1.inputMoney(1000000)

print(countYoung1.getDates())