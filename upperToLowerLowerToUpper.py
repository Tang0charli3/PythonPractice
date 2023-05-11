# WAP to convert upper to lower or lower to upper.
a = "Tango"
b = ""
for i in range(len(a)):

    if a[i].isupper():
       c = a[i].lower()
       b += c
    else:
        c = a[i].upper()
        b += c
print(b)
