class Car():
    wheels = 4
    longChassis = 260
    brodChassis = 130
    torOff = False

    def startUp(self):
        self.torOff = True
    
    def statusCar(self):
        if(self.torOff):
            return "El carro esta funcionando"
        else:
            return "El carro no Arranca"

mazda = Car()
renault = Car()

#mazda.startUp()

print("El estado del carro: ",mazda.statusCar())