
# Numbers
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)

# Strings
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

a, b = 3, 4
print(a,b)

# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)

# change this code
mystring = None
myfloat = None
myint = None

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)