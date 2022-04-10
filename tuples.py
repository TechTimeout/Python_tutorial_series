#A tuple is a collection that is ordered ,allow duplicate values, unchangeable and heterogeneous.
# Tuples are written with round brackets.

fruits=('apple', 'banana','coconut','apple','apple',2,4,34,True)
print(type(fruits))
print(fruits)

print(fruits[0],fruits[3],fruits[5])

print(fruits[2:])
print(fruits[:4])
print(fruits[2:5])

#fruits[3]=88   This is not allowed as tuples are immutable/unchangeable.

fruits=list(fruits)
fruits[3]=88
fruits=tuple(fruits)
print(fruits)

names=('Tech timeout')
print(type(names))
names=('Tech timeout',)
print(type(names))

objects=('apple', 'banana','coconut','apple','apple',2,4,34,True)
objects_list=list(objects)
objects_list.append('car')
objects_list.remove('apple')
objects=tuple(objects_list)
print(objects)


first_tup=('Tea','house',345.56,False)
second_tup=('Coffee','rose',45,True)
third_tup=first_tup+second_tup
print(third_tup)
print(first_tup*2)

new_tup=('Tea','house',345.56,False)
for i in new_tup:
    print(i)

j=0
while j<len(new_tup):
    print(j,new_tup[j])
    j+=1

new_tup=('Tea','house',345.56,False,False,False)
print(new_tup.count(False))
print(new_tup.count('rat'))
print(new_tup.index('house'))
# print(new_tup.index('hat'))  returns error


(var_one,var_two)=('Tea','house')
print(var_one,var_two)
(var_one,*var_two)=('Tea','house',345.56,False,False,False)
print(var_one,var_two)