# Numeric datatypes are float, integer and complex 

from tkinter import Y


myNumber=2
print(myNumber)
print(type(myNumber))


myNumber=456.993
print(myNumber)
print(type(myNumber))

myNumber=-3+44j
print(myNumber)
print(type(myNumber))


a=-99
b=-873.000
c=-12e2  #-12*100
d=-4e2   #-4*100
e=-2+35.0j

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print(c)
print(d)
print(e)

#python casting
x=777
y=345.90
z=-7+45j

b=int(y)
c=float(x)
d=complex(x)
e=complex(y)

print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))

#boolean datatypes

a=True
b=False
print(type(a))
print(type(b))


c=(1>2)
d=(5==4)
e=(6<7)
f=(3!=3)

print(c)
print(d)
print(e)
print(f)

print(bool(1>2))
print(bool(5==4))
print(bool(6<7))
print(bool(3!=3))

print(bool(0))
print(bool(""))
print(bool())
print(bool(1))
print(bool("Tech timeout"))