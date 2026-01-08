class Person:
    __name = ""
    lastName = ""
    __age = 0
    gender = "sin definir"

    def __init__(self,name,lastName,gender):
        self.__name = name
        self.lastName = lastName

        self.gender = gender

    def verifyAge(self,age):
        if age < 0 or age > 150:
            print("Error en la edad..")
        else:
            self.__age = age


    def walking(self):
        return "La persona "+self.__name+" Esta caminando"
    
    def talking(self):
        return "La persona "+self.__name+" Esta caminando"

    def programming(self):
        return "La persona "+self.__name+" Esta programando"


    def getDates(self):
        return "El nombre es "+self.__name+ \
        " su apellido es "+self.lastName+" su edad es de "+str(self.__age) + \
        " su genero es "+self.gender


print("####################################################")

p1 = Person("felipe","pinto","Masculino")
p1.verifyAge(-20)

print(p1.getDates())

print(p1.programming())
