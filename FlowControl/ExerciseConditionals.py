#declaration
tipeImpositivo = ["7%","15%","21%","35%","45%"]

def verifyTipeImpo(rent):
    index = 0
    if valueRent < 12000:
        index = 0
    elif 12000 <= valueRent and valueRent <= 18000:
        index = 1 
    elif 18000 <= valueRent and valueRent <= 35000:
        index = 2
    elif 350000 <= valueRent and valueRent <= 70000:
        index = 3
    else: index = 4
        
    return index



valueRent = float(input())
index = verifyTipeImpo(valueRent)
message = "A la renta ",valueRent, " le correspode un ", tipeImpositivo[index]," de tipo impositivo"

print(message)