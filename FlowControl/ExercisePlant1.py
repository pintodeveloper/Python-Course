countries = {}

while(True):
    country = input("Ingrese un pais: ")
    if(country.lower() == "salir"):
        break
    city = input("Ingrese una ciudad: ")
    if(city.lower() == "salir"):
        break
    
    new_list = countries.setdefault(country,[city])
    
    if new_list != [city]:
        countries[country].append(city)
    
    
print(countries)
    