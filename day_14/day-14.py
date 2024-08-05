# Day 14 Exercises

from functools import reduce
import string


def square(x):
    return x**2

def cube(x):
    return x**3

def absolute(x):
    if x >= 0:
        return x
    else :
        return -(x)
    
def higher_order_function(type):
    if type =='square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
    
result = higher_order_function('square')
print(result(3))
result = higher_order_function('cube')
print(result(3))
result = higher_order_function('absolute')
print(result(-3))

def add_ten():
    ten =10
    def add(num):
        return num+ten
    return add

closure_result = add_ten()
print(closure_result(5))
print(add_ten()(12))

def greeting():
    return 'Welcome to Python'
def uppercase_decarator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

g = uppercase_decarator(greeting)
# print(g())

def uppercase_decarator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decarator
def greeting():
    return 'Welcome to Python'
# print(greeting())


def uppercase_decarator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def split_string_decarator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decarator
@uppercase_decarator   
def greeting():
    return 'Welcome to Python'
print(greeting()) 


def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

numbers = [1,2,3,4,5]
def square(x):
    return x**2
numbers_squared =  map(square,numbers)
print(list(numbers_squared))
numbers_squared_l = map(lambda x : x**2,numbers)
print(list(numbers_squared_l))

numbers_str = ['1','2','3','4','5']
numbers_int = map(int, numbers_str)
print(list(numbers_int))

names = ['Vasantan', 'Renukah','Inbachelvan','Iniyarooban','Ilaveanthan']
def change_upper(name):
    return name.upper() 

name_uppercase = map(change_upper,names)
print(list(name_uppercase))   

l_uppercase = map(lambda name: name.upper(),names)
print(list(l_uppercase))

def is_even(num):
    if num%2 == 0 :
        return True
    else :
        return False
    
even_numbers = filter(is_even,numbers)
print(list(even_numbers))

odd_numbers = filter(lambda num : True if num%2 ==1 else False,numbers)
print(list(odd_numbers))

alpha = ['a','b','c','d','e']
def add_two(x,y):
    return x+y

total = reduce(add_two,alpha)
print(total)


# Level 1 Exercise


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)

for name in names:
    print(name)

for number in numbers:
    print(number)

# Level 2

print(list(map(lambda country : country.upper(),countries)))
print(list(map(lambda x : x**2,numbers)))
print(list(map(lambda name : name.upper(),names)))
print(list(filter(lambda country : True if 'land' in country else False ,countries)))
print(list(filter(lambda country : True if len(country) ==6 else False,countries)))
print(list(filter(lambda country : len(country) >=6 ,countries)))
print(list(filter(lambda country: country[0] == 'E', countries)))


print(list(filter(lambda word : word.isalpha(),numbers_str)))
print(reduce(lambda x,y: x+y,numbers))

import countries

def categorize_countries(country_list,word):
    my_list = []
    for country in country_list:
        
        if word in country :           
            my_list.append(country)
    return my_list

              
country_list = countries.countries
print(categorize_countries(country_list,'land'))
print(categorize_countries(country_list,'stan'))

def countries_counter(country_list):
    key_country = {}
    

    for countries in country_list:
        first_letter = countries[0]
        if first_letter in key_country:
            key_country[first_letter] +=1
        else :
            key_country[first_letter] = 1
    return key_country

print(countries_counter(country_list))

#level 3

import countries_data

def sort_countries_category(country_data,type):
    my_list = []
    c_list = []
    for country in country_data:
        my_list.append(country[type])
        c_list.append(country['name'])
    combine_list = zip(my_list,c_list)
    sorted_list = sorted(combine_list)
    return sorted_list

countries_dat = countries_data.countries


print(sort_countries_category(countries_dat,'name'))
print(sort_countries_category(countries_dat,'capital'))
print(sort_countries_category(countries_dat,'population'))


def ten_most_spoken(countries_data):
    languages = {}

    for country in countries_data:
        for language in country['languages']:
            if language in languages:
                languages[language] += 1
            else:
                languages[language] = 1 

    sorted_languages = sorted(languages.items(),key=lambda x: x[1],reverse=True)
    ten_most_spoken = sorted_languages[:10]
    return ten_most_spoken

print(ten_most_spoken(countries_dat))

def ten_most_populated(countries_data):
    population = {}

    for country in countries_data:
        c_names = country['name']
        popu = country['population']
        population[c_names] = popu
        

    sorted_population = sorted(population.items(),key=lambda x: x[1],reverse=True)
    ten_most_populated = sorted_population[:10]
    return ten_most_populated

print(ten_most_populated(countries_dat))
