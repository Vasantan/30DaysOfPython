# Day 7: Exercise

#Level 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
others =  {'Instagram','Whatsapp'}
it_companies.update(others)
print(it_companies)
it_companies.remove('Google')
print(it_companies)
it_companies.discard('Apple')
print(it_companies)

#level 2
C=A.union(B)

print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
D=B.union(A)
print(C)
print(D)
print(A.symmetric_difference(B))
del A
print(B)


#level 3

ages = set(age)
print(len(age))
print(len(ages))
sentence= 'I am a teacher and I love to inspire and teach people.'
n_sentence = sentence.split()
tpl= tuple(sentence)
n_tpl = set(n_sentence)
print(tpl)
print(len(tpl))

print(len(n_tpl))


sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
unique_words = set(words)
number_of_unique_words = len(unique_words)

print(f"Number of unique words: {number_of_unique_words}")