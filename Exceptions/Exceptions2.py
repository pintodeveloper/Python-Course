def divide():
    
    try:
        n1 = float(input("Ingrese el 1 #: "))
        n2 = float(input("Ingrese el 2 #: "))
        number = n1/n2
        print("El resultado es "+str(number))
    except ZeroDivisionError:
        print("No puedes dividir entre 0")
    except ValueError:
        print("Error dato no valido. intenta de nuevo")
    finally:
        print("Entramos en finally")
    
    

divide()

print("Calculo finalizado.")