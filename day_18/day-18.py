import re
from collections import Counter

txt ='I love to teach python and javascript'
match = re.match('I love to teach',txt,re.I)
print(match)
span = match.span()
print(span)
start,end = span
print(start,end)
substring= txt[start:end]
print(substring)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match = re.search('first',txt,re.I)
print(match)
span = match.span()
print(span)
start,end = span
print(start,end) 
substring = txt[start:end]
print(substring)

matches = re.findall('language',txt,re.I)
print(matches)

matches = re.findall('python', txt)
print(matches)

matches = re.findall('Python|python',txt)
print(matches)

matches = re.findall('[Pp]ython',txt)
print(matches)

match_replaced = re.sub('Python|python','JavaScript',txt,re.I)
print(match_replaced)

match_replaced = re.sub('[Pp]ython', 'Javascript',txt,re.I)
print(txt)
print(match_replaced)

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%','',txt)
print(matches)


txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''

print(re.split('\n',txt))

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern,txt)
print(matches)
matches = re.findall(regex_pattern,txt,re.I)
print(matches)
regex_pattern = r'[Aa]pple'
matches = re.findall(regex_pattern,txt)
print(matches)

regex_pattern = r'[Aa]pple | [Bb]anana'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern,txt)
print(matches)

regex_pattern = r'\d'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern,txt)
print(matches)

regex_pattern = r'\d+'
matches = re.findall(regex_pattern,txt)
print(matches)

regex_pattern = r'[a].'
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern,txt)
print(matches)

regex_pattern = r'[a].+'
matches = re.findall(regex_pattern,txt)
print(matches)

regex_pattern = r'[a].*'
matches = re.findall(regex_pattern,txt)
print(matches)

regex_pattern = r'[Ee]-?mail'
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
matches = re.findall(regex_pattern,txt)
print(matches)


txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern =r'\d{4}'
matches = re.findall(regex_pattern,txt)
print(matches)

regex_pattern = r'\d{1,4}'
matches = re.findall(regex_pattern,txt)
print(matches)

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'

regex_pattern = r'[^A-Za-z ]+'  # ^ in set character means negation, not A to Z, not a to z, no space
matches = re.findall(regex_pattern, txt)
print(matches)


regex_pattern = r'[^A-Za-z]+'
matches = re.findall(regex_pattern,txt)
print(matches)


# Day 18 : Exercise
#Level 1

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
regex_pattern = r'\b\w+\b'
words = re.findall(regex_pattern,paragraph.lower())
mfw = Counter(words)
most_common_word = mfw.most_common()
print(most_common_word)

txt ='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'
regex_pattern = r'-?\d+'
points = re.findall(regex_pattern,txt)
sorted_points = sorted(map(int,points))
distance = sorted_points[-1] -sorted_points[0]
print(distance)

regex_pattern = r'^[A-Za-z_]\w*$'
def is_valid_variable(word):
    return bool(re.match(regex_pattern,word))
    
print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean_text = re.sub(r'[#!%$@&;]','',sentence)
print(clean_text)
