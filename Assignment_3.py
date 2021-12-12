#SOLVED EXAMPLES
# 3.1
'''While purchasing certain items, a discount of 10% is offered if the quantity purchased is more than
1000. If quantity and price per item are input through the keyboard, write a program to calculate the
 total expenses'''

qty = int(input('Enter value of quantity'))
price = float(input('Enter value of price'))
if qty > 1000:
    dis = 10
else:
    dis = 0
totexp = qty * price - qty * price * dis / 100
print(('Total expenses = Rs.' + str(totexp)))

# 3.2
''' In a company an employee is as under:
If the basic salary is less than Rs.1500, then HRA = 10% of basic salary and DA=90% of basic salary.
If his salary is either equal to or above Rs.1500, then HRA = Rs.500 and DA = 98% of basic salary.
If the employees salary is input through the leyboard write a program to find his gross salary.'''

bs = int(input('Enter value of bs:'))
if bs > 1000:
    hra = bs * 15/100
    da = bs * 95/100
    ca = bs * 10/100
else:
    hra = bs * 10 / 100
    da = bs * 90/ 100
    ca = bs * 5 / 100
gs = bs + da + hra + ca
print('Gross Salary= Rs.'+str(gs))

# 3.3
'''Percentage marks obtained by a student are input through the keyboard the keyboard.
The student gets a division as per the following rules:
Percentage above or equal to 60 - First division
Percentage between 50 and 59 - Second division
Percentage between 40 and 49 - Third division
Percentage less than 40 - Fail
Write a program to calculate the division obtained by the student.'''

per = int(input('Enter value of percentage:'))
if per >= 60:
    print('First Division')
elif per >= 50:
    print('Second Division')
elif per >= 40:
    print('Third Division')
else:
    print('Fail')

# 3.4
'''A company insures its drivers in the following cases:
- If the driver is married.
- If the driver is unmarried, male & above 30 years of age.
- If the driver is unmarried, female & above 25 years of age.
In all other cases, the driver is not insured. If the marital status, sex and age of
the driver are the inputs, write a program to determine whether the driver should
 be insured or not.'''

ms = input('Enter marital status:')
s = input('Enter sex:')
age = int(input('Enter age:'))
if (ms == 'm') or (ms == 'u' and s == 'm' and age > 30) \
        or (ms == 'u' and s == 'f' and age > 25):
    print('Insured')
else:
    print('Not Insured')

# 3.5
'''Suppose there are four flag variables w, x, y, z. Write a program to check in
multiple ways whether ine of them is true.'''

# Different ways to test multiple flags
w,x,y,z = 0,1,0,1
if w == 1 or x == 1 or y == 1 or z == 1:
    print('True')
if w or x or y or z:
    print('True')
if any((w,x,y,z)):
    print('True')
    if 1 in (w,x,y,z):
        print('True')



#********UnSolved Programs**********
#3.2.1
''' Any integer is input thruough the keyboard. Write a program to find out whether
 it is an odd number or even number'''


# Determine whether number is odd or even
x = int(input('Enter any number:'))
j = 2
if x % j == 0:
    print('Even Number')
else:
    print('Odd Number')

#3.2.2
'''Any year is input through the keyboard. Write a program to dermine whether the year
is a leap year or not.'''

# Determine whether year is leap or not
year = int(input('Enter a year:'))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(year,'is a Leap Year')
        else:
            print(year,'is not a Leap Year')
    else:
        print(year,'is a Leap Year')
else:
    print(year,'is not a Leap Year')

#3.2.3
''' If ages of Ram, Shyam and Ajay are input through the keyboard, write a program to
determine the youngest of the three.'''

ram_age = int(input('Enter Ram\'.s age:'))
shyam_age = int(input('Enter Shyam\'.s age:'))
ajay_age = int(input('Enter Ajay\'.s age:'))
if ram_age < shyam_age and ram_age < ajay_age:
    print('Youngest is Ram')
elif shyam_age < ram_age and shyam_age < ajay_age:
    print('Youngest is Shyam')
elif ajay_age < ram_age and ajay_age < shyam_age:
    print('Youngest is Ajay')

#3.2.4
'''Write a program to check whether a triangle is valid or not, when the three angles
of the triangle are entered through the keyboard. A trianle is valid if the sum of all
the three angles is equal to 180 degrees'''

# Determine whether triangle is valid or not
x = int(input('Enter angle no.1 :'))
y = int(input('Enter angle no.2:'))
z = int(input('Enter angle no.3:'))
sum_of_angles = x + y + z
if sum_of_angles == 180:
    print('Valid Triangle')
else:
    print('Inalid Triangle')


#3.2.5
# Write a program to find the absolute value of a number entered through the keyboard.

# Obtain absolute value of a number
x = int(input('Enter any number:'))
if x < 0:
    y = x*(-1)
else:
    y = x
print('Absolute value of',x,'is',y)

#3.2.6
'''Given the length and breadth of a rectangle, write a program to find whether the area of the
rectangle is greater then its perimeter. For example, the area of the rectangle with length = 5
and breadth = 4 is greater than its perimeter'''

#Determine whether area of rectangle is grater than its perimeter
length = int(input('Enter the length of rectangle:'))
breadth = int(input('Enter the breadth of rectangle:'))
area = length * breadth
perimeter = 2 * (length + breadth)
print('Area=',area,'Perimeter=',perimeter)
if area > perimeter:
    print('Area of Rectangle is grater than perimeter')
else:
    print('Perimeter of rectangle is greater than area')

#3.2.7
'''Given three points(x1,y1),(x2,y2) and (x3,y3), write a program to check if all the
three points fall on one straight line.'''

# Determine whether 3 points are collinear
x1 = int(input('Enter the co-ordinates of x1:'))
y1 = int(input('Enter the co-ordinates of y1:'))
x2 = int(input('Enter the co-ordinates of x2:'))
y2 = int(input('Enter the co-ordinates of y2:'))
x3 = int(input('Enter the co-ordinates of x3:'))
y3 = int(input('Enter the co-ordinates of y3:'))
if x1 == x2 and x2 == x3:
    print('Collinear')
elif x1 != x2 and x2 != x3 and x3 != x1:
    # Calculate Slope of line between each pair of points
    s1 = (float(abs(y2 - y1))) / (float(abs(x2 - x1)))
    s2 = (float(abs(y3 - y2))) / (float(abs(x3 - x2)))
    s3 = (float(abs(y3 - y1))) / (float(abs(x3 - x1)))
if s1 == s2 and s2 == s3:
    print('Three points are Collinear')
else:
    print('Three point are Non Collinear')



#3.2.8
'''Given the coordinates(x,y) of center of a circle and its radius, write a program that
will determine whether a point lies inside the circle, on the circle or outside the circle'''

# Determine whether point lies inside, outside or on the circle
import math
centerX = int(input('Enter X coord. of center of circle:'))
centerY = int(input('Enter Y coord. of center of circle:'))
radius = int(input('Enter radius of circle:'))
print('Enter coordinates of point:')
pointX = int(input('Enter the X coord. of point'))
pointY = int(input('Enter the Y coord. of point'))
xDiff = centerX - pointX;
yDiff = centerY - pointY;
distance = math.sqrt((xDiff * xDiff) + (yDiff * yDiff))

if distance == radius:
    print('Point is on the circle')
elif distance < radius:
    print('Point lies inside the circle')
else:
    print('Point lies outside the circle')

#3.2.9
'''Given a point (x,y), write a program to find out if it lies on the
X-axis, Y=axis or on the orign '''

#Determine where a point lies in coordinate system
x = int(input('Enter X Coord of the point:'))
y = int(input('Enter Y Coord of the point:'))
if x == 0 and y == 0:
    print('Point is the origin')
elif x == 0 and y != 0:
    print('Point lies on the Y axis')
elif x != 0 and y == 0:
    print('Point lies on the X axis')
else:
    if x > 0 and y > 0:
        print('Point lies in the First Quadrant')
    elif x < 0 and y > 0:
        print('Point lies in the Second Quadrant')
    elif x < 0 and y < 0:
        print('Point lies in the Third Quadrant')
    else:
        print('Point lies in the Fourth Quadrant')

#3.2.10
'''A year is entered through the keyboard, write a program to determine whether the year
is leap or not. Use the logical opertors and and or '''

# Determine whether year is leap or not
year = int(input('Enter a year:'))
if(year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print(year,'is a leap year')
else:
    print(year,'is not a leap year')


#3.2.11
'''If the three sides of a triangle are entered through the keyboard, write a program to
check whether the triangle is valid or not. the triangle is valid if the sum of two sides
is greater than the largest of the three sides'''

#Determine whether triangle is valid or not
s1 = int(input('Enter the 1st side of triangle:'))
s2 = int(input('Enter the 2nd side of triangle:'))
s3 = int(input('Enter the 3rd side of triangle:'))
if s1 + s2 <= s3 or s2 + s3 <= s1 or s1 + s3 <= s2:
    print('Invalid Triangle')
else:
    print('Valid Triangle')

#3.2.12
'''If the three sides of a triangle are entered through the keyboard, write a program
to check whether the triangle is isosceles, equilateral, scalene or right angled triangle.'''

# Determine the type of triangle
s1 = int(input('Enter the 1st side of triangle:'))
s2 = int(input('Enter the 2nd side of triangle:'))
s3 = int(input('Enter the 3rd side of triangle:'))
if s1 + s2 <= s3 or s2 + s3 <= s1 or s1 + s3 <= s2:
    print('The side do not form a triangle')
else:
    if s1 != s2 and s2 != s3 and s3 != s1:
        print('Scalene Triangle')
    if s1 == s2 and s2 != s3:
        print('Isosceles triangle')
    if s2 == s3 and s3 != s1:
        print('Isosceles triangle')
    if s1 == s3 and s3 != s2:
        print('Isosceles triangle')
    if s1 == s2 and s2 == s3:
        print('Equilateral triangle')
a = (s1 * s1) == (s2 * s2) + (s3 * s3)
b = (s2 * s2) == (s1 * s1) + (s3 * s3)
c = (s3 * s3) == (s1 * s1) + (s2 * s2)
if a or b or c:
    print('Right-angled triangle')

