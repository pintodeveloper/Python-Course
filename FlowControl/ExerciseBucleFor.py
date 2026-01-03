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

    