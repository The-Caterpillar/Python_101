# Comprehensions in Python

l = [1,2,3,4,5,6,7,8,9,10]

x = [x for x in l if x%2==0]
print(x)

s='fuhdcilacjlsgvuaeiou'
x = [y for y in s if y in 'aeiou']
print(x)

z = { x for x in l if x%2!=0}
print(z)

#  DICTIONARY COMPREHENSIONS
l1 = [1,3,5,7,9,0]

d1 = {x:x**3 for x in l1}
print(d1)


#  F-strings in Python
pi = 3.14159263659
print(f"The value of pi is: {pi:.2f}")

d2 = {x:f"ID{x}" for x in range(5)}
print(d2)

d3 = dict(zip(d1,d2))
print(d3)

d3 = dict(zip(l,l1))
print("zipped d3: ",d3)