#Day 12 : Exercise
import random
import string 


def random_user_id():
    characters = string.ascii_letters+string.digits
    my_list = []
    for i in range(6):
        char = random.choice(characters)
        my_list.append(char)
    result1 = ''.join(my_list)

    my_list2 = random.choices(characters,k=6)

    result2 =''.join(my_list2)


   

    return result1, result2
print(random_user_id())

def user_id_gen_by_user():
    char_num = int(input("Key in number of character for ID : "))
    num_of_id = int(input("Key in number of ID's : "))

    characters = string.ascii_letters+string.digits
    my_list = []
    for item in range(num_of_id):
        result = ''.join(random.choices(characters,k=char_num))
        my_list.append(result)
    return '\n'.join(my_list)

# print(user_id_gen_by_user())


def rgb_color_gen():
    r = random.randint(0,256)
    g = random.randint(0,256)
    b = random.randint(0,256)
    result = f'rgb({r},{g},{b})'
    return result

print(rgb_color_gen())


def list_of_hexa_colors(num):
    my_list = []
    hexa_character = string.digits +'abcdef'

    for i in range(num):
        hexa = "#"+''.join(random.choices(hexa_character,k=6))
        my_list.append(hexa)
    
    return my_list
print(list_of_hexa_colors(6))

def list_of_rgb(num):
    my_list =[]
    for i in range(num):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        rgb = f"rgb({r},{g},{b})"
        my_list.append(rgb)
    return my_list

print(list_of_rgb(5))

def generate_colors(type,num):
    if type == 'hexa':
        return list_of_hexa_colors(num)
    elif type == 'rgb':
        return list_of_rgb(num)
    else :
        return "Invalid color request"
    
print(generate_colors('rgb',2))


# Level 3

def shuffle_list1(my_list):
    shuffled_list = my_list[:]
    random.shuffle(shuffled_list)
    print(shuffled_list)

def shuffle_list2(my_list):
    result = random.sample(my_list,2)
    print(result)

my_list = [1,2,3,4]
shuffle_list1(my_list)
print(my_list)
shuffle_list2(my_list)

def seven_random_numbers1():
    m_list = [0,1,2,3,4,5,6,7,8,9]
    result = random.sample(m_list,7)
    return "".join(map(str,result))

def seven_random_numbers2():
    unique_numbers = set()
    while len(unique_numbers)<7:
        number = random.randint(0,9)
        unique_numbers.add(number)
    return ''.join(map(str,unique_numbers))

print(seven_random_numbers1())
print(seven_random_numbers2())
