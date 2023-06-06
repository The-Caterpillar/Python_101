#  List in python = arrays in C++

l = [1,5,7]
print(l) # Prints the whole list with the brackets
print(l[0]) # Prints element at index 0


# Slicing of lists
m = [1,2,3,4,5,6,7]
x= m[0:4]
print(x)



# Adding a new element in the list (at the end)
m.append(13)
print(m)



# Merging two lists - extend
b = [20,100]
l.extend(b)
print(l)



# Inserting an element at desired index
l.insert(2,100)
print(l)


# Sorting a list
l.sort()
print(l)


# delete an element from the desired position
l.pop(2)
print(l)


#  count occurrences of an element
o = [1,2,3,3,3,2,1,100,99,101,100]
a = o.count(100)
print(a)

#  length of a list
print(len(o)) # 11

#  Sum of all elements of o
b = sum(o)
print(b)


#  Copy a list (ek k pichhe ek)
L = [1,2,3]
x = L*3 
print(x)


 #  for loop for lists:
for i in range(len(L)):
	print(L[i])

# Taking input in list
new = []
print("Enter how many numbers you wish to input: ")
n = int(input())

for i in range(n):
	a = int(input())
	new.append(a)

print("The new list is: ",new)