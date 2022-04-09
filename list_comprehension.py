first_list=['Car','Truck','Bike','Cart']
second_list=[x for x in first_list]
print(second_list)

# newlist=[expression for item in terable if condition==True]

third_list=[x.upper() for x in first_list if x!='Car']
fourth_list=[x for x in range(4)]
print(fourth_list)
fourth_list=[x for x in range(2,4)]
print(fourth_list)

fifth_list=["Hello!" for x in range(0,5)]
print(fifth_list)