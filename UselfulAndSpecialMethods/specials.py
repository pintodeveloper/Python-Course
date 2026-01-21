class Person():
    
    dates_info = []
    
    def __init__(self,*dates):
        
        for i in dates:
            self.dates_info.append(i) 
        self.getDates(self.dates_info)
    
    def getDates(self, info):
        for d in info:
            print(d)
       
##El metodo str pasa a string la informacion del objeto


    

p1 = Person("felipe","pinto",20)

print(p1)