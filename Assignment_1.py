# SOLVED EXAMPLES OF 
# 1.1 Demonstrate use of integer types and operators that can be used on them
print(3/4)
print(3%4)
print(3//4)
print(3**4)

a = 10 ; b = 25 ; c = 15 ; d = 30 ; e = 2 ; f = 3 ; g = 5
w = a+b-c
x = d**e
y = f%g
print(w,x,y)
h = 9999999999999999999999999999
i = 54321
print(h*i)

# 1.2 
print("use of float, complex and bool types and operations that can be used on them")
# float
i = 3.5
j = 1.2
print(i%j)
# complex
a = 1+2j
b = 3*(1+2j)
c = a*b
print(a)
print(b)
print(c)
print(a.real)
print(a.imag)
print(a.conjugate())
print(a)
# bool
x = True
y = 3>4
print(x)
print(y)

# 1.3
print("Demonstrate how to convert from one number type another")
# convert into int
print(int(3.14))
a = int('485')
b = int(768)
c = a+b
print(c)
print(int('1011', 2))
print(int('341', 8))
print(int('21',16))

# convert to float
print(float(35))
i = float('4.85')
j = float('7.68')
k = i+j
print(k)

# convert to complex
print(complex(35))
x = complex(4.85, 1.1)
y = complex(7.68, 2.1)
z = x+y 
print(x)

# convert to bool
print(bool(35))
print(bool(1.2))
print(int(True))
print(int(False))


# 1.4
print("A program that makes use of built-in mathematical functions")
print(abs(-23))
print(pow(2,4))
print(min(10,20,30,40))
print(max(10,-10,30,50))
print(divmod(17,3))
print(bin(64), oct(64), hex(64))
print(round(2.567), round(2.5678, 2))

#1.5
print("A program that makes use of functions in the math module")
from abc import abstractproperty
import math
x = 1.5357
x1=9
print(math.pi, math.e)
print(math.sqrt(x))
print(math.factorial(x1))
print(math.log(x))
print(math.log10(x))
print(math.exp(x))
print(math.trunc(x))
print(math.floor(x))
print(math.ceil(x))
print(math.trunc(-x))
print(math.floor(-x))
print(math.ceil(-x))
print(math.modf(x))

#1.6
print("A program that generates float and integer random numbers")
import random
import datetime
random.seed(datetime.time())
print(random.random())
print(random.random())
print(random.randint(10,100))

#1.7
print("Identify string, list, tuple, set or dictionary ")
print(type({10,20,30.5}))
print(type([1,2,3.14,'Nagpur']))
print(type({12:'Simple', 43:'Complicated', 13:'Complex'}))
print(type("Check it out"))
print(type(3+2j))

# ****Unsolved Programs****
#1.2.1
print("A program that swaps values without a third variable")
a = 8
b = 23
a,b=b,a
print('a=',a)
print('b=',b)

#1.2.2
print("Use of Trignometric fuctions in math module")
import math
a = math.pi/6
print("The value of sine of pi/6 is", end='')
print(math.sin(a))
print("The value of cosine of pi/6 is", end='')
print(math.cos(a))

#1.2.3
print("A program that generate 5 random numbers in the range 10 to 50")
import random
import time
random.seed(6)
for i in range(5):
    print(random.randint(10,50))
print()
t = int(time.time())
random.seed(t)
for i in range(5):
    print(random.randint(10,50))

#1.2.4
import math
print(math.floor(-2.8))
print(math.trunc(-2.8))
print(math.ceil(-2.8))
print(math.floor(-0.5))
print(math.trunc(-0.5))
print(math.ceil(-0.5))
print(math.floor(1.5))
print(math.trunc(1.5))
print(math.ceil(1.5))
print(math.floor(2.9))
print(math.trunc(2.9))
print(math.ceil(2.9))

#1.2.5
print("Convert Fahrenheit into Centigrade")
farh = 212
cen = ((farh-32)*5/9)
print(farh,"farenheit =",cen,"centigrade")

