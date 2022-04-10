# dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable, 
# heterogeneous and does not allow duplicates.
# Dictionaries are written in curly brackets and have keys and values 


my_dict={'car':3,'house':7,'rice':8}
print(my_dict)
my_dict['car']=20
print(my_dict)

my_dict[78.555]=True

print(type(my_dict))
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print('house' in my_dict)
print('house' in my_dict.keys())

print(7 in my_dict)
print(7 in my_dict.values())


my_dict={'car':3,'house':7,'rice':8,'rice':9}
print("----keys----")
for i in my_dict.keys():
    print(i)
print("---values----")
for j in my_dict.values():
    print(j)

print("----items---")
for i,j in my_dict.items:
    print(i,j)

first_dict={'Tech timeout':100,'California':67,True:'Not false'}
second_dict=first_dict
first_dict['Tech timeout']=300
print(first_dict)
print(second_dict)

first_dict={'Tech timeout':100,'California':67,True:'Not false'}
second_dict=first_dict.copy()
first_dict['Tech timeout']=300
print(first_dict)
print(second_dict)
