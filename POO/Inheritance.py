class Person():
    
    def __init__(self,name,lastName,age):
        self.name = name
        self.lastName = lastName
        self.age = age
    
    def getDates(self):
        return "Nombre " + self.name + " Apellido "+ \
            self.lastName + " Edad "+ str(self.age)

    def talking(self):
        return "Estoy Hablando.."
    
    def eating(self):
        return "Estoy comiendo.."
    
    def thinking(self):
        return "Estoy pensando.."
    
    def walking(self):
        return "Estoy caminando.."
    
class Student(Person):
    
    def __init__(self, name, lastName, age,school):
        #self.name = name
        #self.lastName = lastName
        #self.age = age
        #El metodo Super(), sirve cuando hay sobre escritura y se necesita info del padre
        
        super().__init__(name, lastName, age)
    
        self.school = school
    
    def getDates(self):
        return super().getDates() + " Escuela "+self.school
    
    def studying(self):
        return "Estoy estudiando.."
    
person1 = Person("Felipe","Pinto",20)

#queremos saber el colegio en el cual estudio.

student1 = Student("Andrey","Uribe",21,"San Francisco")

print(person1.getDates())
print(student1.getDates())