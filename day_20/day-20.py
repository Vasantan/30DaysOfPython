import requests
from collections import Counter
import re

url = 'https://www.gutenberg.org/files/1112/1112-0.txt'



def most_frequent_words(url,num):
    response = requests.get(url)
    txt = response.text
    regex_pattern = r'\b\w+\b'
    all_words = re.findall(regex_pattern,txt.lower())
    word_counter = Counter(all_words)
    most_frequent_words = word_counter.most_common(num)
    return most_frequent_words

print(most_frequent_words(url,10))


def cat_detail(url):
    response = requests.get(url)
    cat_details = response.json()
   
    min_list = []
    max_list = []
    mean_list = []
    for item in cat_details:
        min,space,max = item['weight']['metric'].split()
        min = int(min)
        max = int(max)
        mean = (min+max)/2
        min_list.append(min)
        max_list.append(max)
        mean_list.append(mean)

    sorted_min_list =  sorted(min_list)
    sorted_max_list = sorted(max_list)
    sorted_mean_list = sorted(mean_list)
    return sorted_max_list

url = 'https://api.thecatapi.com/v1/breeds'
print(cat_detail(url))


def cat_detail(url):
    response = requests.get(url)
    cat_details = response.json()
    
    min_list = []
    max_list = []
    mean_list = []
    for item in cat_details:
        min,space,max = item['life_span'].split()
        min = int(min)
        max = int(max)
        mean = (min+max)/2
        min_list.append(min)
        max_list.append(max)
        mean_list.append(mean)

    sorted_min_list =  sorted(min_list)
    sorted_max_list = sorted(max_list)
    sorted_mean_list = sorted(mean_list)
    return sorted_max_list

url = 'https://api.thecatapi.com/v1/breeds'
print(cat_detail(url))


def country_and_breed(url):
    response = requests.get(url)
    cat_details = response.json()
    
    country_list = []
    breed_list = []
    
    for item in cat_details:
        country = item['origin']
        breed = item['name']
        country_list.append(country)
        breed_list.append(breed)
    country_and_breed_list = list(zip(country_list,breed_list))


    
    return country_and_breed_list

url = 'https://api.thecatapi.com/v1/breeds'
print(country_and_breed(url))    


url = 'https://restcountries.com/v3.1/all'
api_pull = requests.get(url)
api_data = api_pull.json()

def largest_countries(api_data,num=10):

    sorted_countries = sorted(api_data, key= lambda x: x.get('area',0),reverse =True)
    largest_countries = [(country['name']['official'],country['area']) for country in sorted_countries[:10]] 
    return largest_countries

def spoken_languages(api_data,num=10):

    languages_counter = Counter()

    for country in api_data:
        languages = country.get('languages',{})
        for language in languages.values():
            languages_counter[language] +=1

    most_spoken_language = languages_counter.most_common(num)
    return most_spoken_language

def total_number_of_languages(api_data):
    language_set = set()

    for country in api_data:
        languages = country.get('languages',{})
        language_set.update(languages.values())
    
    total_languages = len(language_set)
    return total_languages


largest_countries = largest_countries(api_data)
most_spoken_languages = spoken_languages(api_data)
total_languages = total_number_of_languages(api_data)

# Print results
print("10 Largest Countries by Area:")
for country, area in largest_countries:
    print(f"{country}: {area} sq km")

print("\n10 Most Spoken Languages:")
for language, count in most_spoken_languages:
    print(f"{language}: spoken in {count} countries")

print(f"\nTotal Number of Distinct Languages: {total_languages}")




