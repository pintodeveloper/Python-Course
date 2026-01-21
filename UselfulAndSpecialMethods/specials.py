class Person():
    def __init__(self,name,lastName,age):
        self.name = name
        self.lastName = lastName
        self.age = age

##El metodo str pasa a string la informacion del objeto


    def __str__(self):
        
        return "Datos de la persona: \n"+self.name +"\n Apellido: " +self.lastName + "\n Edad: " + str(self.age)

p1 = Person("felipe","pinto",20)

print(p1)