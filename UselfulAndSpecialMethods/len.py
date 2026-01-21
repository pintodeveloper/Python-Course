class Agenda():
    
    def __init__(self):
        self.myAgenda = {}
        
    def addPeople(self,name,phone):
        self.myAgenda[name] = phone
        
    def __len__(self):
        return len(self.myAgenda)
            
agendaPersonal = Agenda()

agendaPersonal.addPeople("pinto","316444620")
agendaPersonal.addPeople("pabon","216444620")
agendaPersonal.addPeople("plata","316434620")
agendaPersonal.addPeople("sumalave","316477620")

print(len(agendaPersonal))