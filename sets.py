# A set is a collection that is unordered, heterogeneous, doesn't allow duplicates and unindexed.
# Sets are written in curly brackets.



fruits={'apple','mango','cherry','guava','apple'}
print(fruits)
print(type(fruits))
# print(fruits[0]) returns error as sets are unindexed

for i in fruits:
    print(i)

print(i in fruits)

myset={'apple','mango','cherry','guava','apple',34,45,True}
newset={'Car','house',4554,3443,77}
myset.update(newset)
print(myset)
myset.add('666')
print(myset)
myset.update({'Tech timeput',23456})
print(myset)
myset.update(['Tech timeput',23456])
print(myset)
myset.remove('guava')
print(myset)
del myset
# print(myset) return error because myset has been deleted


myset={'apple','mango','apple',34.5,45,True}
newset={'Car','mango',34.45,3443,77}

returnset=myset.symmetric_difference(newset) #retuens a new set,that contains 
                                           # only the elements that are NOT present in both the sets 

unionset=myset.union(newset)  #retur  a new set containing all the items from both the sets

myset.intersection_update(newset)  #will keep only the items that are present in both the sets

# yourset=myset+newset  returns error


