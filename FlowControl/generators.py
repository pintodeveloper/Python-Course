#Nos devuelven los valores de una manera
#muy calmada, con pasiencia



def generarPars(limit):
    
    num=1
    

    
    while num < limit:
        
        yield num*2
        
        num+=1
        
sucetionPars = generarPars(6)

for i in sucetionPars:
    print(i)