a = 'hello'
b = 'hello'
if id(a) == id(b):
    print('True')
else:
    print('False')

a = 'hai@123'
b = 'hai@123'
if id(a) == id(b):
    print('True')
else:
    print('False')

a = 'Apple'
b = 'apple'
if id(a) == id(b):
    print('True')
else:
    print('False')

a = 'our college'
b = 'our college'
if id(a) == id(b):
    print('True')
else:
    print('False')

a = 'This isstring'
b = 'This is also string'
if id(a) == id(b):
    print('True')
else:
    print('False')
