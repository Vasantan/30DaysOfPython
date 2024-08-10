f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

with open ('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

with open ('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')

with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in newly creatd file')


import os

if os.path.exists('./files/examples.txt'):
    os.remove('./files/example.txt')
else :
    print('This file does not exist')


import json

person_json = '''{
    "name": "Vasantan",
    "country":"Malaysia",
    "city" : "Johor Bahru",
     "skills": ["Python","C++"] 
     }'''

person_dct = json.loads(person_json)
print(type(person_dct))
print(type(person_json))
print(person_dct)
print(person_dct['name'])

convert_json = json.dumps(person_dct,indent=4)
print(type(convert_json))
print(convert_json)

with open('./files/json_example.json','w', encoding='utf-8') as f:
    json.dump(person_dct,f,ensure_ascii=False,indent=4)

import csv

with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f,delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'column names are : {", ".join(row) }')
            line_count+=1
        else :
            print(f'\t{row[0]} is a teachers. He lives in {row[2]},{row[1]}.')
            line_count+=1
    print(f'Number of lines : {line_count}.')



import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag',root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ',child.tag)


#Day 19 : Exercise
#Level 1
 
def count_number_of_lines_words(txt_file):
    with open(txt_file) as f:
        txt = f.read()
        word_count = len(txt.split())

    with open(txt_file) as f:
        lines = f.readlines()
        line_count =len(lines)
        return f'Number of words in speech in {word_count} and number of lines is {line_count}.'

print(count_number_of_lines_words('./data/obama_speech.txt'))
print(count_number_of_lines_words('./data/michelle_obama_speech.txt'))
print(count_number_of_lines_words('./data/donald_speech.txt'))

from collections import Counter

def most_spoken_languages(qty,filename):
    with open(filename,encoding='utf-8') as f:
        countries_data =json.load(f)
        lang_list = []
        for country in countries_data:
            for language in country['languages']:
                lang_list.append(language)
        spoken_language = Counter(lang_list)
        most_spoken = spoken_language.most_common(qty)
    return most_spoken    


    

print(most_spoken_languages(10,filename='./data/countries_data.json'))

def most_populated_countries(qty,filename):
    with open(filename,encoding='utf-8') as f:
        countries_data =json.load(f)
        population_list = []
        for country in countries_data:
            dct = {'country':country['name'],'population':country['population']}
            population_list.append(dct)
    
    sorted_population = sorted(population_list,key=lambda x: x['population'],reverse=True)
    most_populated = sorted_population[:qty]
    return most_populated    

print(most_populated_countries(10,filename='./data/countries_data.json'))
import re

def get_email(file):
    with open(file, 'r', encoding='utf-8') as f:
        txt = f.read()

        email_regex_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
        
        email_list= re.findall(email_regex_pattern,txt)

        email_set = set(email_list)

    
    return email_set


file_path = r'C:\Users\Vasantan\Documents\Git\30DaysOfPython\data\email_exchanges_big.txt'
print(get_email(file_path))



def find_most_common_words(file, num):
    with open(file) as f :
        regex_pattern = r'\b[A-Za-z]+\b'
        txt = f.read()
        words = re.findall(regex_pattern,txt)
        common_words = Counter(words)
        most_comman_words = common_words.most_common(num)
        return most_comman_words
    


print(find_most_common_words('./data/obama_speech.txt',10))
print(find_most_common_words('./data/michelle_obama_speech.txt',10))
print(find_most_common_words('./data/donald_speech.txt',10))

def clean_word_list(file):

    with open(file) as f:
        txt = f.read().lower()
    regex_pattern = r'[^\w\s]'
    clean_text = re.sub(regex_pattern,'',txt)
    clean_words = clean_text.split()

    return clean_words

txt1 = clean_word_list('./data/obama_speech.txt')
txt2 = clean_word_list('./data/michelle_obama_speech.txt')

from stop_words import stop_words

def remove_support_words(txt1,txt2):

        
    filtered_text1 = [word for word in txt1 if word not in stop_words]
    filtered_text2 = [word for word in txt2 if word not in stop_words]

    return filtered_text1, filtered_text2

filtered_txt1,filtered_txt2 = remove_support_words(txt1,txt2)

def check_similarity(txt1,txt2):
    set_txt1 = set(txt1)
    set_txt2 = set(txt2)

    intersection = set_txt1.intersection(set_txt2)
    union = set_txt1.union(set_txt2)

    similarity = len(intersection)/len(union)
    return intersection

    return set_txt1

print(check_similarity(filtered_txt1,filtered_txt2))

print(find_most_common_words('./data/romeo_and_juliet.txt',1))


import csv

file_path= './data/hacker_news.csv'
def count_lines(file,regex_pattern):
    count = 0
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            line = ' '.join(row)
            matches = re.search(regex_pattern,line)
            if matches:
                count+=1
            
            
    return count

print(count_lines(file_path,r'\b[Pp]ython\b'))
print(count_lines(file_path,r'\b[Jj]ava[Ss]cript\b'))

def count_lines_java_not_javascript(file):
    count = 0
    with open(file,newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            line = ' '.join(row)
            if re.search(r'\b[Jj]ava',line) and not re.search(r'\b[Jj]ava[Ss]cript\b',line):
                count+=1
            
    return count

java_not_javascript_count = count_lines_java_not_javascript(file_path)
