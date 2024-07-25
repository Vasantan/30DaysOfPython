#Day 3 Exercise
age = 41
height = 176
com = 1+1j
base = int(input("Enter triangle base:"))
height = int(input ("Enter triangle height:"))
area = 0.5*base*height
print(f"The area of the triangle is : {area}.")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
perimeter = a+b+c
print(f"The perimeter of the triangle is : {perimeter}.")
r_length = int(input("Provide rectangular length:"))
r_width = int(input("Enter rectangular width : "))
r_area = r_length*r_width
r_perimeter = 2*(r_length+r_width)
print(f"The area of rectangle is : {r_area}")
print(f"Perimeter for rectangle perimeter is :{r_perimeter}")
pi = 3.14
c_radius = int(input("Provide circle radius:"))
c_area = pi*(c_radius**2)
c_circum = 2*pi*c_radius
print(f"The circle area is :{c_area}.")
print(f"The circle circumference is : {c_circum}")
cord_1 = [2,2]
cord_2 = [6,10]
slope = (cord_2[1]-cord_1[1])-(cord_2[0]-cord_1[0])
print("Slope :",slope)
y =-1
while y!= 0:
    x=int(input("Provide X value that can make y = 0 :"))
    y=(x**2)+6*x+9
    print(y)
print("len(python)==len(dragon) : ",len("python")==len("dragon"))
print("Is 'on' in 'python and dragon: ",'on'in 'python' and 'on' in 'dragon')
print("is jargon in 'I hope this course is not full of jargon'",'jargon' in 'I hope this course is not full of jargon' )
print("No 'on' in 'python and dragon? ",'on'not in 'python' and 'on' not in 'dragon')
print(len('python'))
print(float(len('python')))
print(str(float(len('python'))))
print("Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.  ",7//3 ==int(2.7))
print("Check if type of '10' is equal to type of 10  ",type('10')==type(10))
print("Check if int('9.8') is equal to 10  ", int(9.8)==10)
hour=int(input("Enter hour :"))
rate = int(input("Enter rate per hour :"))
print(f"Your weekly earning is {hour*rate}.")
year = int(input("Enter number of years you have lived:"))
print(f"You have lived for {31536000*year} seconds.")
for i in range(1,6):
    print(f"{i} 1 {i} {i**2} {i**3}")
    

