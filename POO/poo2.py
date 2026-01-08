class Person:
    name = ""
    lastName = ""
    age = 0
    gender = "sin definir"

    def __init__(self,name,lastName,age,gender):
        self.name = name
        self.lastName = lastName
        self.age = age
        self.gender = gender

    def walking(self):
        return "La persona "+self.name+" Esta caminando"
    
    def talking(self):
        return "La persona "+self.name+" Esta caminando"

    def programming(self):
        return "La persona "+self.name+" Esta programando"


    def getDates(self):
        return "El nombre es "+self.name+ \
        " su apellido es "+self.lastName+" su edad es de "+str(self.age) + \
        " su genero es "+self.gender
    

p1 = Person("felipe","pinto",20,"Masculino")
print(p1.getDates())
print(p1.talking())
