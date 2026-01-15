class Person():
    def talk(self):
        return "Hablo como una persona"

class Worker():
    def talk(self):
        return "Hablo como un trabajador"

class Director():
    def talk(self):
        return "Hablo como un director"

def hazlehablar(listPerson):
    for person in listPerson:
        print(person.talk())

def talking(objeto):
    print(objeto.talk())

Antonio = Person()
Maria = Worker()
Ana = Director()


print(Antonio.talk())
print(Maria.talk())
print(Ana.talk())


print("----------------------------")

listPerson=[Antonio,Maria,Ana]

hazlehablar(listPerson) #un objeto puede cambiar de forma en ejecución
talking(Ana)