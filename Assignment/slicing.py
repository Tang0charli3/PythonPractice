s = "python is a programming language"

# Using negative indexing
print(s[-20:-9:1])

# extract "si nothyp" using combination
b=s[0:9:1]
print(b[::-1])

# write all the possibilities to fetch "alternative characters in reverse direction"
a = "Tango Charlie"
b = a[::-2]
print(b)

a = "Tango Charlie"
b = ""
for i in range(len(a)-1, -1, -2):
    b += a[i]
print(b)