myDates = ("felipe77",'february', 18, 2005)

print(myDates)

#Se puede volver una tupla en lista

myList = list(myDates)

print(myList)


newTuples = tuple(myList)

print(newTuples)


##to know if an element is in a tuple

print("18" in myDates)

#to know how many times an element in a tuple

countElement = newTuples.count('felipe77')

print("La cantidad de veces que esta repetido en la tupla es de: "+ str(countElement))

sizeNewTuples = str(len(newTuples))

print('la cantidad de elementos que contiene la tupla es de: '+sizeNewTuples)


#desempaquetar tupla

n, month, day , age = newTuples

print(n,"\n")
print(month,"\n")
print(day,"\n")
print(age,"\n")


"""


#Tambien se puede volver una lista en tupla

#Acceder a un elemento de la tupla
print(myDates[1])


#Acceder a un rango de elementos de la tupla
print(myDates[0:2])
#Las tuplas son inmutables, no se pueden cambiar sus elementos
#myDates[0] = "newValue" #Esto dara un error    
#Pero se puede reasignar la tupla completa
myDates = ("newUser",'march', 25, 2010)
print(myDates)  
print(len(myDates))  #Imprime la longitud de la tupla

#Desempaquetado de tuplas
username, month, day, year = myDates
print(username)
print(month)   
print(day)
print(year)
print(type(myDates))  #Imprime el tipo de dato, en este caso sera 'tuple'
print(type(myList))   #Imprime el tipo de dato, en este caso sera 'list'
print(type(newTuple)) #Imprime el tipo de dato, en este caso sera 'tuple'
print(myDates.count('newUser'))  #Cuenta cuantas veces aparece 'newUser' en la tupla
print(myDates.index(25))  #Devuelve el indice del primer elemento con valor 25
print(sorted(myDates))  #Devuelve una lista ordenada de los elementos de la tupla
print(min(myDates))  #Devuelve el elemento minimo de la tupla
print(max(myDates))  #Devuelve el elemento maximo de la tupla
print(sum([day, year]))  #Devuelve la suma de los elementos numericos de la tupla
print(any([day, year]))  #Devuelve True si al menos un elemento es verdadero
print(all([day, year]))  #Devuelve True si todos los elementos son verdaderos   
print(myDates[::-1])  #Imprime la tupla en orden inverso
print(myDates + ("extraValue",))  #Concatena una nueva tupla a la existente
print(myDates * 2)  #Repite la tupla dos veces

print("february" in myDates)  #Verifica si 'february' esta en la tupla
print("april" not in myDates)  #Verifica si 'april' 
#no esta en la tupla

#Iterar sobre los elementos de la tupla
for element in myDates:
    print(element)
#Iterar sobre los indices y elementos de la tupla
for index, element in enumerate(myDates):
    print(f"Index: {index}, Element: {element}")
#Anidar tuplas
nestedTuple = (myDates, ("anotherUser", 'april', 10, 2015))
print(nestedTuple)


"""