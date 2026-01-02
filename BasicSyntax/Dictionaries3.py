tel = {'jack': 4098,'sape':4139}
tel['guido'] = 4127

print(tel.keys())

print(tel.get('jack'))

newList = list(tel)
print(newList)


print(tel)
sorted(tel)

print(tel)




############Notations differens

newDict = dict([
    ('sape', 4139),
    ('guido', 4127),    
    ('jack', 4098)
    ])

print(newDict)

newList2 = {x: x**2 for x in (2,4,6)}

print(newList2)

newList3 = dict(coco=77,pinto=77,felipe=77)
print(newList3)