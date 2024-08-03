# Day 11 Level 1 Exercise

import keyword
import countries_data
from collections import Counter

def add_two_numbers(num1,num2):
    total = num1+num2
    return total

print(f"Sum of two numbers : {add_two_numbers(3,3)}")


def area_of_circle(radius, pi=3.14):
    area = pi*radius**2
    return area

print(f"Area of circle: {area_of_circle(2)}")


def add_all_nums(*nums):
    total = 0
    for num in nums:
        
        if isinstance(num,(int,float)):
            total+=num
        else:
            print(f"Invalid input{num}. All input must be numbers")
            return "Error : All input must be numbers"

    return total

r=4
print(add_all_nums(1,3,4,r))

def convert_celsius_to_fahrenheit(c_temp):
    f_temp = (c_temp*9/5)+32
    return f_temp

print(f"5' in celcius equal to {convert_celsius_to_fahrenheit(5)} in fahrenheit.")


def check_season(month):
    
    autumn = ['September','October','November']
    winter = ['January','February','December']
    spring = ['March','April','May']
    summer = ['June','July','August']

    if month in autumn:
        season='Autumn'
    elif month in winter:
        season= 'Winter'
    elif month in spring:
        season = "Spring"
    elif month in summer:
        season = 'Summer'
    else : 
        print('Invalid month')
    return season

print(f"Its {check_season('July')} right now")


def calculate_slope(x1,y1,x2,y2):
    try :
        slope = (y2-y1)/(x2-x1)
        return slope
    except ZeroDivisionError:
        return "Undefined vertical line"
    
slope = calculate_slope(1,2,3,4)
print("Slope :",slope)


def print_list(p_list):
    for i in p_list:
        print(i)

p_list = [1,2,4,"bell"]
print_list(p_list)

def reverse_list(lst):
    r_list = lst[::-1]
    return r_list

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))

def capitalize_list_items(c_list):
    capitalized_list =[]
    for item in c_list:
        capitalized_list.append(item.capitalize())

    return capitalized_list

c_list = ['was', 'I got new','day30']
print(capitalize_list_items(c_list))

def add_item(n_list,item):
    i_list = [item]
    added_list = n_list +i_list
    return added_list

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat'))     
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))     

def remove_item(mylist1,myitem1):
    index = mylist1.index(myitem1)
    mylist1.pop(index)
    return mylist1

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]


def sum_of_numbers(mynum):
    total = 0
    for index in range(1,mynum+1):
        total += index
    return total

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

def sum_of_odds(mynum):
    total = 0
    for index in range(1,mynum+1):
        if index%2 ==1:
            total+=index
    return total

print(sum_of_odds(5))  # 15
print(sum_of_odds(10)) # 55
print(sum_of_odds(100))


def sum_of_even(mynum):
    total = 0
    for index in range(1,mynum+1):
        if index%2 ==0:
            total+=index
    return total

print(sum_of_even(5))  # 15
print(sum_of_even(10)) # 55
print(sum_of_even(100))



# Level 2

def evens_and_odds(mynum):
    even_count = 0
    odd_count = 0

    for num in range(0,mynum+1):
        if num%2 ==0:
            even_count+=1
        elif num%2 ==1:
            odd_count+=1

    return "# The number of odds are {} \n# The number of evens are {}.".format(odd_count,even_count)

print(evens_and_odds(100))

def factorial(mynum):
    if mynum <0 or not isinstance(mynum,int):
        return "invalid input"
    
    if mynum == 0:
        return 1
    factor = 1 
    for i in range(1,mynum+1):
        factor *=i
        
    return factor

print(factorial(6))


def is_empty(value):
    if value:
        return False
    else :
        return True

print(is_empty(""))          # Output: True (empty string)
print(is_empty([]))          # Output: True (empty list)
print(is_empty({}))          # Output: True (empty dictionary)
print(is_empty(None))        # Output: True (None is considered empty)
print(is_empty([1, 2, 3]))   # Output: False (non-emp
        
def calculate_mean(mylist):
    mean = sum(mylist)/len(mylist)
    return mean

print(calculate_mean([1, 2, 3, 4, 5]))  # Output: 3.0

def calculate_median(mylist):
    sorted_list = sorted(mylist)
    mid = len(sorted_list)//2

    if len(mylist)%2 ==1:
        median = sorted_list[mid]
    elif len(mylist)%2 ==0:
        median = (sorted_list[mid-1]+sorted_list[mid])/2

    return median

print(calculate_median([1, 3, 3, 6, 7, 8, 9]))  # Output: 6



# Level 3 

def is_prime(num):
    if num<=1:
        return False

    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
        
    return True

print(is_prime(7))  # Output: True
print(is_prime(10))  # Output: False


def is_unique(my_list):
    seen =set()
    for item in my_list:
        if item in seen:
            return False
        seen.add(item)
    return True

my_list =[1,2,3,4,5]
print(is_unique(my_list))
my_list_with_duplicates = [1, 2, 3, 4, 5, 3]
print(is_unique(my_list_with_duplicates))  # Output: False


def is_same_datatype(my_list):
    if not my_list:
        return True


    data_set = type(my_list[0])
    for item in my_list[1:]:
        if data_set!= type(item):
            return False
    return True


print(is_same_datatype([1, 2, 3, 4]))      # Output: True (all integers)
print(is_same_datatype([1, 2, '3', 4]))    # Output: False (contains a string)
print(is_same_datatype(['a', 'b', 'c']))   # Output: True (all strings)

def if_same_datatype(my_list):
    length = len(set(type(item) for item in my_list))
    return length <= 1

print(if_same_datatype([1, 2, 3, 4]))      # Output: True (all integers)
print(if_same_datatype([1, 2, '3', 4]))    # Output: False (contains a string)
print(if_same_datatype(['a', 'b', 'c']))   # Output: True (all strings)


def valid_python_variable(var1):
    result = var1.isidentifier() and not keyword.iskeyword(var1)
    return result

print(valid_python_variable('my_var'))  # Output: True
print(valid_python_variable('2var'))    # Output: False
print(valid_python_variable('_var'))    # Output: True
print(valid_python_variable('for'))     # Output: False (reserved keyword)


def most_spoken_languages(c_data):
    c_list = []
    for item in c_data:
        for language in item['languages']:
            c_list.append(language)

    counted_list = Counter(c_list)
    sorted_list = counted_list.most_common(10)
    return sorted_list


c_data = countries_data.countries
print(most_spoken_languages(c_data))

def most_populated_countries(c_data):
    p_list = []
    for item in c_data:
        p_list.append([item['population'],item['name']])

    sorted_p_list = sorted(p_list, key=lambda x:x[0],reverse=True)
    ten_most_populated =sorted_p_list[:10]

    return ten_most_populated 

print(most_populated_countries(c_data))
