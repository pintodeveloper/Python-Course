vowel = ['a','e','i']

vowel.extend(['o','u'])

vowel.append('f')

vowel.remove('f')

vowel.append("pinto")


print(vowel)

print(vowel[1:5])

print(vowel[::-1])

#del vowel[-1]

print(vowel)

print(vowel[::2])


numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

#print(numbers[::3]) # every 3rd element [1,4,7,10]

#print(numbers[1::3]) # from index 1, every 3rd element [2,5,8]

#print(numbers[2::4]) # from index 2, every 4th element [3,7]

#print(numbers[::-2]) # reverse every 2nd element [10,8,6,4,2]

print(numbers[3::3]) # from index 3, every 3rd element [4,7,10,13]

print(numbers[4::4]) # 5 9 13

print(numbers[5:12:2]) # from index 5 to 11, every 2nd element [6,8,10,12]