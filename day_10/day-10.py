from collections import Counter 
import countries
import countries_data

# Day 10 : Exercise 
list = [0,1,2,3,4,5,6,7,8,9,10]

for i in list:
    print(i)

count =0
while count<=10:
    print(count)
    count+=1

while count>= 0:
    print(count)
    count-=1

for index in range(1,8):
    result = (index)*'#'
    print(result)
    
for index in range(1,9):
    text =''
    for item in range(1,9):
        text+='# '
    print(text)

for index in range(0,11):
    print(f'{index} x {index} = {index**2}')

skills=['Python', 'Numpy','Pandas','Django', 'Flask']
for item in skills:
    print(item)

for num in range(0,101):
    if num%2==0 :
        print(num)
for num in range(0,101):
    if num%2==1 :
        print(num)


#Exercise level 2
total=0
for num in range(0,101):
    total+=num

print(total)

even_total=0
odd_total =0
for num in range(0,101):
    if num%2 == 0:
        even_total+=num
    if num%2 == 1:
        odd_total+=num
print(f"The sum of all evens is {even_total}. And the sum of all odds is {odd_total}.")


#Exercise 3

for country in countries.countries:
    if 'land' in country:
        print(country)

fruits =  ['banana', 'orange', 'mango', 'lemon']

length =len(fruits)
for i in range(-1,-length-1,-1):
    print(fruits[i])

lg_set = set()
lg_list = []
pp_list =[]

print(lg_set)
for country in countries_data.countries :
    for language in country['languages']:
        lg_set.add(language)
        lg_list.append(language)
    pp_list.append([country['population'],country['name']])

sorted_list = sorted(pp_list,reverse =True)
top_populated = sorted_list[:10]
lg_counter= Counter(lg_list)
most_spoken = lg_counter.most_common(10)
print(most_spoken)
print(len(lg_set))
print(top_populated)