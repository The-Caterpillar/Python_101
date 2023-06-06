# Strings in python
s = "Hi I am Saraswati"
print(s[0])

# Length of string
print(len(s))


#  String slicing
t = s[0:5]
print(t)

t = s[0:]
print(t)

t = s[:5]
print(t)

#  How many times b string occurs in a sstring?
a = "Hi hi Hi HI HI Hi Hi Hi Hi Hello"
b = "Hi"

count = a.count(b)
print(count)


# Searching for a substring in a string, returns -1 if
# substring is not present in the parent string
b = "Saraswati"
f = s.find(b)
print("Saraswati appears at index:",f," in string s")
# Another way to check for a substring
if(b in a):
	print("Yes")
else:
	print("No")
#  Printing every character
for h in b:
	print(h)
# Convert every character of string in lowercase
b  = b.lower()
print(b)

#  Removing spaces from between the words of strings
test = "Remove spaces from between the string"
test = test.replace(" ","")
print(test)
