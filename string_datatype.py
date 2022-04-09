a="Tech timeout"
a='Tech timeout'

b='''Tech timeout 
is a youtube channel'''

c="""Tech timeout 
is a channel to learn coding"""


print(b)
print(c)

a="Hello, world!"

print(a[0])
print(a[-1])

print(a[1],a[2],a[3],a[4],a[5])

for x in a :
    print(x)

print("llo" in a)
print("f" in a)

print(len(a))
print(len("My name is anonymous"))

#string slicing
print(a[1:6])
print(a[2:8])
print(a[:])
print(a[2:8:2])
print(len(a[2:8:2]))

print(a[3:])
print(a[:9])


a="Hello, world!"
b="AA, BB, CCC, DDD"
print(a.lower())
print(a.upper())
print(a.split(" "))
print(b.split(","))

a="This is a boy,"
b=" This is a girl."

print(a+b)
print(a+"  It is a good day  "+b)


a=" a boy"
b="a house"
print(f"This is {a}. These is {b}")
print("This is {0}. These is {1}".format(a,b))
print("This is {}. These is {}".format(a,b))


a="This is a youtube channel called \"Tech timeout\""
print(a)
a="This is a youtube channel called \n Tech timeout\n "
print(a)
a="This is a youtube channel called \\n Tech timeout \\n "
print(a)
