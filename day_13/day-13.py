#Day 13 Exercise

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
only_negative_zero = [num for num in numbers if num<=0]
print(only_negative_zero)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flatten_list  = [number for row in list_of_lists for numbers in row for number in numbers]
print(flatten_list)

tupple_list = [(num,num**0,num**1,num**2,num**3,num**4, num**5) for num in range(11)]
print(tupple_list)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
f_country = [[item[0],item[0][:3],item[1]] for items in countries for item in items]
print(f_country)

dict_country = [{'country': item[0],'city': item[1]} for items in countries for item in items]
print(dict_country)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

full_name = [item[0]+' '+item[1] for name in names for item in name]
print(full_name)

slope = lambda x1,y1,x2,y2 : (y2-y1)/(x2-x1) if x1!= x2 else None
y_intercept = lambda x,y,m : y-m*x

print(slope(1,2,3,8))
print(y_intercept(1,2,4))