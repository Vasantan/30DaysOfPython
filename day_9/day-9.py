#Day 9 exercise

def drive_eligibilty():

    age = int(input('Hi\nEnter your age : '))

    if age>= 18:
        print ('You are old enough to learn to drive.')
    else :
        n_age = 18-age
        print(f'You need {n_age} to learn to drive.')

# drive_eligibilty()

def who_is_older():
    age = int(input('Hi\nEnter your age : '))
    my_age = 41
    
    if my_age>age:
       
        if my_age-age== 1  :
            print("We have one year different in age")
        else :
            print(f"I am {my_age-age} older than you" )
    elif my_age<age:
        print(f"I am {age-my_age} younger than you" )

    else:
        print("We have same age")

# who_is_older()

def compare_number():
    num1 = int(input('Enter number one: '))
    num2 = int(input("Enter number two : "))

    if num1>num2:
        print(f'{num1} greater than {num2}')
    elif num1<num2:
        print(f'{num1} less than {num2}')
    else :
        print(f'{num1} equal to {num2}')

# compare_number()

#level 2

def grading():
    score = int(input('Hi\nEnter your score : '))

    if score >= 0 and score <=49:
        print("Your grade is F")
    elif score >= 50 and score <=59:
        print("Your grade is D")
    elif score >= 60 and score <=69:
        print("Your grade is C")
    elif score >= 70 and score <=79:
        print("Your grade is B")
    elif score >= 80 and score <=100:
        print("Your grade is A")
    else : 
        print("your score looks invalid")
    
# grading()

def season():
    month = input("Provide current Month: ")
    autumn = ['September','October','November']
    winter = ['January','February','December']
    spring = ['March','April','May']
    summer = ['June','July','August']

    if month in autumn:
        print("Its Autumn")
    elif month in winter:
        print("Its Winter")
    elif month in spring:
        print('Its Spring')
    elif month in summer:
        print('Its Summer')
    else : 
        print('Invalid month')

# season()

def is_fruits():

    fruits = ['banana','orange','mango','lemon']

    loop =True
    while loop == True:
        print("*Remark : Type q if wish to quit")
        fruit = input(" Key in fruits to check in list: ")
        if fruit == 'q':
            loop = False
        elif fruit  not in fruits:
            fruits.append(fruits)
            print(fruits)
        elif fruit in fruits:
            print('That fruit already exist in the list')
# is_fruits()

def personel():
    person={'first_name': 'Vasantan',
    'last_name': 'Govinda Raju',
    'age': 41,
    'country': 'Malaysia',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Jaya Putra',
        'zipcode': '81100'}}
    
    if 'skills' in person.keys():
        mid = len(person['skills'])//2+1
        print(person['skills'][mid-1])
        if 'Python' in person['skills']:
            print('There is python')


personel()