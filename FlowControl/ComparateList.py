def comparateList(v1,v2):
    if(len(v1) != len(v2)):
        return False
    
    for i in range(len(v1)):
        if(v1[i] != v2[i]):
            return False
        
    
    return True
     



list1 = ["A","B","C","D","E"]
list2 = ["A","B","C","D","E"]

equals = comparateList(list1,list2)

print(equals)