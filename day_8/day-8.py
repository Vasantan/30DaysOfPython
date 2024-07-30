#Day 8 : Exercise
dog = {}
dog['name'] = 'Johny'
dog['color'] = 'White'
dog['breed'] =  'street'
dog['legs'] = 4
dog['age'] = 5
print(dog)

student = {'name':'iniyarooban', 'gender': 'Male', 'age': 10, 'is_married': False,'Country':'Malaysia'}
print(len(student))
print(type(student['age']))
print(student.keys())
print(student.values())
print(student.items())
del student['gender']
print(student)
student.popitem()
print(student)
del student


