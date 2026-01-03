capitalice = {"china": "pekin","India": "Nueva delhi","Indonesia": "Yarda","Banglades": "Dacca"}

for password, value in capitalice.items():
    print(password + " --> "+value)
    


for password in capitalice:
    print("Esta es la clave: "+password)
    
    
for value in capitalice:
    v = capitalice[value]
    print("Este es el valor: "+v)