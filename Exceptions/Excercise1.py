#Agg elemnt in a list

#10 names
#is some name is repet, el programa lanzara una exception
#the tipe ValueError, show error "Error, Este nombre ya se ha introducido"
# no se guardara el nombre repetido en la lista
#show list camplet

"""
julia
felipe
ninfa
drigelio
leidy
angela
andry
isabel
omar
mariela
"""

namesList = []

def veryPerson(name):
    print("estoy en la funcion")
    if(name in namesList):
        raise ValueError ("El nombre ya esta en la lista..")
    else:
        namesList.append(name)
        return ("Registro de nombre exitoso...")
    

while(True):
    name = input("Ingresa un nombre: ")
    print("voy en el ciclo")
    try: 
        veryPerson(name)
    except ValueError:
        print("Ingresa un nombre que no este repetido. ")
    
    if len(namesList) == 10 : break
    

for n in namesList:
    print(n)
    