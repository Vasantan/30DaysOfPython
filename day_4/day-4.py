#Day 4  : Exercise

string1,string2,string3,string4 = 'Thirty','Days','Of','Python'
space = ' '
full = string1+space+string2+space+string3+space+string4
print(full)
string5,string6,string7 = 'Coding',"For",'All'
full2= string5+space+string6+space+string7
print(full2)
company = 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.swapcase())
print(company)
code = 'thirty days of python'
print(code.capitalize())
print(code.title())
print(code.swapcase())
print(company[0])
print(company[0:6])
print(company.index('Coding'))
print(company.find('For'))
print(company.rfind('All'))
print('Coding' in company)
print(company.replace('Coding','Python'))
p_code = 'Python for Everyone'
print(p_code.replace('Everyone','All'))
print(company.split())
print(len(company)-1)
print(company[10])
print(''.join(word[0] for word in company.split()))
print(''.join(word[0] for word in p_code.split()))
print(company.find('C'))
print(company.find('F'))
print(company.rfind('l'))
sentence=  'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rfind('because'))
print(sentence.rindex('because'))
print(sentence.replace(' because',''))
print(sentence.index('because'))
print(sentence[:sentence.index('because')]+sentence[sentence.index('because')+len('because because because'):])
sub_string='Coding'
print(company.startswith('Coding'))
print(company.endswith('coding'))
print('   Coding For All      '.strip())
print('# '.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))
print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\tCity\nVasantan\t41\tMalaysia\tJohor Bahru')
radius = 10
area = 3.14*radius*2
print(f'The area of a circle with radius {radius} is {area:.2f} meters square.')
a=8
b=6

print('{} + {} = {}'.format(a,b,a+b))
print('{} - {} = {}'.format(a,b,a-b))
print('{} * {} = {}'.format(a,b,a*b))
print('{} / {} = {}'.format(a,b,round(a/b,2)))
print('{} % {} = {}'.format(a,b,a%b))
print('{} // {} = {}'.format(a,b,a//b))
print('{} ** {} = {}'.format(a,b,a**b))
