# WAP to check middle element of the list is even or not.
a=[1, 2, 3, 4, 5]
b=int(len(a)/2)
if a[b] % 2 == 0:
    print("Middle element is even")
else:
    print("Middle element is Odd")
