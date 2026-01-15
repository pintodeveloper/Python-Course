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
        
        Person.__init__(self,name, lastName, age)
    
        self.school = school
    
    def getDates(self):
        return super().getDates() + " Escuela "+self.school
    
    def studying(self):
        return "Estoy estudiando.."
    
    
class Worker(Person):
    def __init__(self, name, lastName, age,company):
       
        Person.__init__(self,name, lastName, age)
    
        self.company = company
    
    def getDates(self):
        return super().getDates() + " Empresa "+self.company
    
    def working(self):
        return "Estoy trabajando.."
    
class Director(Worker,Student):
    def __init__(self, name, lastName, age, company,school,bonus):
        Worker.__init__(self,name, lastName, age, company)
        Student.__init__(self,name,lastName,age,school)
        self.bonus = bonus
    
    def getDatesPersonals(self):
        return super().getDates() + " Bonus: "+str(self.bonus)

    def lead(self):
        return "Estoy dirigiendo.."

person1 = Person("Pipe","Ponto",20)
student1 = Student("Ninfa","Pinto",62,"SF")
print(person1.getDates())
print(student1.getDates())

print("---------------------------")
    
worker1= Worker("Felipe","Pinto",20,"Figma")
print(worker1.getDates())

director = Director("Andrey","Pinto",21,"UFPSO","Ufpso",500000)

print(director.getDates())