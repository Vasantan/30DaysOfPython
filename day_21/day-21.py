class Person:
    def __init__(self,firstname='Vasantan',lastname='Govinda raju',age =41,country= 'Malaysia',city='Johor Bahru'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skill =[]
    
    def person_info(self):
        return f"{self.firstname} {self.lastname} is {self.age} year old."

    def add_skill(self,skill):
        self.skill.append(skill)
p1 = Person('Vasantan','Govinda Raju',42,'Malaysia','Johor Bahru')
print(p1.firstname)
print(p1.lastname)
print(p1.age)
print(p1.country)
print(p1.city)

print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())


p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('Javascript')
print(p1.skill)


print(p2.skill)

class Student(Person):
    def __init__(self,firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender =gender
        super().__init__(firstname,lastname,age,country,city)

    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'


s1 = Student('Inba','vasantan',12,'Malaysia','JB')
print(s1.person_info())
print(s1.firstname)

s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skill)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skill)

#Day 21 Exercise
from collections import Counter
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

class Statistics:
    def __init__(self,ages):
        self.ages = ages
        self.sorted_ages = sorted(ages)
        
    def sum(self):
        return sum(self.ages)
    
    def count(self):
        return len(self.ages)
    
    def min(self):
        return self.sorted_ages[0]
    
    def max(self):
        return self.sorted_ages[-1]
    
    def range(self):
        return self.max()-self.min()
    
    def mean(self):
        return self.sum()/self.count()
    
    def median(self):
        if self.count() % 2 == 1:
            self.median = self.sorted_ages[self.count()//2]
        else:
            self.median =  (self.sorted_ages[self.count()//2]+self.sorted_ages[(self.count()//2)-1])/2
        return self.median
    
    def mode(self):
        self.age_counter = Counter(self.ages)
        return self.age_counter.most_common(1)
    
    def var(self):
        self.squared_difference = [(age-self.mean())**2 for age in self.ages]
        self.variance = sum(self.squared_difference)/len(self.squared_difference)
        return self.variance  

    def  std(self):
        return self.var()**0.5

    def freq_dist(self):
        total =self.count()
        age_frequency_dist = [((num/self.count())*100,age) for age,num in self.age_counter.items()]
        return age_frequency_dist

data = Statistics(ages)
print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median())
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.
print('Frequency Distribution: ', data.freq_dist())


class PersonAccount:
    def __init__(self,firstname,lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.income = []
        self.expenses = []
        
    def total_income(self):
        return sum(self.income)

    def total_expense(self):
        return sum(self.expenses)

    def account_info(self):
        return f"Account Holder : {self.firstname} {self.lastname} \n"\
               f"Total Income: {self.total_income()}\n" \
               f"Total Expense: {self.total_expense()}\n" \
               f"Account Balance: {self.account_balance()}"
   
    def add_income(self,amount,description):
        self.income.append(amount)

    def add_expense(self,amount,description):
        self.expenses.append(amount)

    def account_balance(self):
        return self.total_income() -self.total_expense()
    
    

person = PersonAccount("John", "Doe")

person.add_income(5000, "Salary")
person.add_income(200, "Freelance Work")
person.add_expense(1500, "Rent")
person.add_expense(300, "Groceries")

print(person.account_info())