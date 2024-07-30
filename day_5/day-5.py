#Day 5 Exercise
#Exercise : Level 1
import countries as c

my_list =[]
print(len(my_list))
my_list=[1,2,3,4,5,6]
print(len(my_list))
print(my_list[0])
print(my_list[3])
print(my_list[-1])
mixed_data_type =  ['Vasantan',41,176,True,'Johor Bahru']
it_companies = ['Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(mixed_data_type)
print(it_companies)
print(len(it_companies))
print(it_companies[0],it_companies[2],it_companies[len(it_companies)-1])
it_companies[3]='Facebook'
print(it_companies)
it_companies.append('IBM')
it_companies.insert(1,'Zoho')
print(it_companies)
it_companies[1].upper()
print(it_companies[1].upper())
'#'.join(it_companies)
print('#'.join(it_companies))
does_in = 'Apple' in it_companies
print(does_in)
does_in = 'Xerox'in it_companies
print(does_in)
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)
first_three = it_companies[:3]
last_three = it_companies[-3:]
print(first_three)
print(last_three)
middle_three = it_companies[2:5]
print(middle_three)
it_companies.remove(it_companies[0])
print(it_companies)
it_companies.remove(it_companies[2])
it_companies.remove(it_companies[-1])
print(it_companies)
del it_companies[:]
print(it_companies)
del it_companies

front_end = ['HTML','CSS','JS','React','Redux']
back_end = ['Node',"Express",'MangoDB']
my_list = front_end+back_end
print(my_list)
full_stack=my_list.copy()
print(full_stack)
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

#Exercise 2

ages = [19,22,19,24,20,25,26,24,25,24]
ages.sort()
print(ages)
min =ages[0]
max= ages[-1]
print(min,max)
length =len(ages)
print(length)
if len(ages)%2 == 1:
    median=ages[length//2 +1]
else:
    median = (ages[length//2] + ages[length//2 -1])/2
print(median)
averange = sum(ages)/length
print(averange)
print(abs(min-averange))
print(abs(max-averange))

print(c.countries[0])
n = len(c.countries)
print(n)
mid=n//2
if n%2 == 0:
    first_countries = c.countries[:mid]
    second_countries = c.countries[mid:]
else:
    first_countries = c.countries[:mid+1]
    second_countries = c.countries[mid+1:]
print(len(first_countries),len(second_countries))
first,second,third,*scandic = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(first)
print(second)
print(third)
print(scandic)