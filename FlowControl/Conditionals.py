def valueAlumn(note):
    evaluation = "desconocidad"
    if(note<5):
        evaluation = "Suspenso"
    elif note > 10:
        evaluation = "Nota incorrecta"
    else:
        evaluation = "aprobado"
    return evaluation

print("Ingrese tu nota: ")
note = float(input())
print(valueAlumn(note))