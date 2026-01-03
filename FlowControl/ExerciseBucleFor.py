number1 = int(input("Ingrese el primer numero: "))    
number2 = int(input("Ingrese el segundo numero: "))

for i in range(number1,number2+1):
    count=0
    for j in range(1,number2+1):
        if(i==1):
            count=2
        if(i%j==0):
            count+=1
    
    if(count==2):
        print(i)   


#############Enfoque 2

num1 = int(input("Introduce el primer numero, por favor: "))
num2 = int(input("Introduce el segundo numero, por favor: "))


def is_prime(number):
    for n in range(2,number):
        if number % n == 0:
            return False
    print(str(number)+" es primo")
    return True

for i in range(num1,num2):
    is_prime(i)
    
    
    
    