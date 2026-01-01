messi = {10: "Messi","name": "Lionel Andrés Messi Cuccittini","mundiales": 'Qatar 2022',
         "Ballons the Gold": {"years": [2009,2010,2011,2012,2015,2019,2021,2023]}}
"""
print(messi.keys())

print(messi.values())


print(messi["Ballons the Gold"])"""


#sets
basket = {'apple','orange','apple','pear','orange','banana'}
#print(basket)
#print('orange' in basket)

a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)
print(a-b)
print(b-a)
print(a|b) #letters in a or b both
print(a & b) #letters in botb a and b
print(a ^ b) #letters in a or b but not both