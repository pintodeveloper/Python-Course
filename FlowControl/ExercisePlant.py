#Introducir paises Y ciudades, hasta que el usuario escriba salir, luego
#Mostrar en un diccionario el pais y sus ciudades correspondientes
from collections import defaultdict

countries = defaultdict(list)

while(True):
    country = input("Escriba un pais: ")
    if country.lower() == "salir":
        break
    city = input("Escriba una ciudad: ")
    if city.lower() == "salir":
        break
    
    countries[country].append(city)
    

print(countries)



