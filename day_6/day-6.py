#Day 6 Exercise

e_tpl = ()
brothers = ('Murugaiah','Kartigesu','Gobi')
sisters = ('Bairavi',)
siblings = brothers + sisters
print(len(siblings))
parents = ('Govinda Raju', 'Pasimah')
family_members =parents+siblings
print(family_members)

father, mother,*sibling = family_members
print(sibling)

fruits = ('banana', 'Mango','Durian')
vegetables = ('Chili', 'beans','cucumber')
animal_product = ('Milk', 'meat', 'egg')
food_stuff_tp = fruits + vegetables + animal_product
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
first_three = food_stuff_tp[0:3]
last_three = food_stuff_tp[-3:]
print(first_three)
print(last_three)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia'in nordic_countries)
print('Iceland' in nordic_countries)
