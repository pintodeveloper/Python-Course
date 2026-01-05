#Nos devuelven los valores de una manera
#muy calmada, con pasiencia



def generarPars(limit):
    
    num=1
    

    
    while num < limit:
        
        yield num*2
        
        num+=1
        
sucetionPars = generarPars(6)

for i in sucetionPars:
    pass
    #print(i)
    
    
#next() -> seria para una sucesion pausada * imprimiria solo el primero



#Funcion con parametros indefinidos
"""  
def capitalice_world(*capitalice):
    for c in capitalice:
        for letter in c:
            yield letter
        

capitalice = capitalice_world("Pekin","Bogota","La valeta","Seul","Honk Kong")

print(next(capitalice))
print(next(capitalice))
print(next(capitalice))
print(next(capitalice))

"""
def capitalice_world(*capitalice):
    for c in capitalice:
        #for letter in c:
        yield from c

capitalice = capitalice_world("Pekin","Bogota","La valeta","Seul","Honk Kong")

print(next(capitalice))
print(next(capitalice))
print(next(capitalice))
print(next(capitalice))