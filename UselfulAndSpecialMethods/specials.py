class Person():
    
    dates_info = []
    
    def __init__(self,**dates):
        
        element = dates.items()
        
        for password,value in element:
            print(password," ",value)
            

    

    

p1 = Person(name="felipe",lastName="pinto",age=20)

