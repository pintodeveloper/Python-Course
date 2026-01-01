person = {
    "age": 20,
    "name": 'Laura Michel Garcia uribe',
    "Nacionalidad": 'Colombiana',
    "Estado civil": 'Soltera',
    "Gustos": 'Sabrosines',
    77: 'felipe77',
    'matriz': ['7','78','48','48','89']
}

#print(person)





del person["age"]

#print(person['matriz'])


estados = ['Norte De santander', 'Santander', 'Valle del cauca', 'Bogota']


citys = {
    
    estados[0]: 'Ocaña',
    estados[1]: 'Bucaramanga',
    estados[2]: 'Cauca',
    estados[3]: 'Cundinamarca',
    
}


#print(citys[estados[0]])
#tuples for create claves

passwords = ["Spanish", "Reino Unido","Colombia","Portugal"]

capitalesMundo={passwords[0]: "Madrid",passwords[1]: "Londres",passwords[2]:"Bogotá",passwords[3]:"Lisboa"}


#print(capitalesMundo)

#to know the keys the dictonaries 

print(capitalesMundo.keys())

#to know the values the dictionaries

print(capitalesMundo.values())

print(len(capitalesMundo))
