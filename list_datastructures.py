# There are 4 types of data structures in Python:
# 1. List 
# 2. set 
# 3. tuple. 
# 4. dictionary. 


# List is  a collection that is ordered, mutable(or changeable) , heterogeneous. 
# Allows duplicate members.

from numpy import append


first_list=['A',123,'hdff',346.88]
print(first_list)
first_list[0]='Tech timeout'
print(first_list)
second_list=[13,14,13,14]
print(second_list)


first_list=[1,4,5,'Tech','timeout','',88.947]
print(first_list[:])
print(first_list[0:5]) #list[startindex:endindex+1]=list containing elements from startindex position to end index position 

print(first_list[-1:-5])
print(first_list[-1:-5:-2])
print(first_list[2:])
print(first_list[:5])



my_list=[1,2,'Apple','peanuts',1,2,4]
my_list[1:3]=[345,456]
print(my_list)


my_list.append('House')  #Appends element to the end of the list
print(my_list) 
my_list,append(['0099',8382,244.344]) #Appends element to the end of the list
print(my_list)
my_list.remove('peanuts')  #removes element from the list
print(my_list)
my_list.insert(3,8876)  #inserts element into list
print(my_list)
my_list.pop()  #pops the rightmost element from the list
print(my_list)


first_list=['Tech','Timeout',1,34,67.77]
second_list=['Rise','shine',234,345]
third_list=first_list+second_list
print(third_list)
first_list.extend(second_list)
print(first_list)

fourth_list=[2,1,5,3,4,88]
fourth_list.sort()
print(fourth_list)
fourth_list.sort(reverse=True)
print(fourth_list)

