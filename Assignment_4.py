#1
# To display Fibonacci series
num = int(input("Enter how many numbers you want to display: "))
a = 0
b = 1
c = 2
print("Fibonnaci Series is")
print(a)
print(b)
while(c<num):
    d = a+b
    print(d)
    a = b
    b = d
    c += 1


#2
# sum of digits
n = int(input("Enter a number:"))
sum = 0
while(n>0):
    rem = n%10
    sum = sum+rem
    n = int(n/10)
print("The sum of digits is: ",sum)


#3
# Reverse of a number
n = int(input("Enter a number: "))
rev = 0
while(n>0):
    rem = n%10
    rev = (rev*10)+rem
    n = int(n/10)
print("Reverse of number is: ",rev)


#4
# Armstrong Number or not
n = int(input("Enter a number: "))
sum = n
sum = 0

while n>0:
    rem = n%10
    sum = sum+rem*rem*rem
    n = int(n/10)
if num == sum:
    print(num," is Armstrang number")
else:
    print(num, " is not a Armstrong number")




#5
# Prime or not
n = int(input("Enter a number: "))
for i in range(2,n+1):
    if n%i==0:
        break
if i == n:
    print(n, ' is a prime number')
else:
    print(n, ' is not a prime number')


    
#6
# All even number between 1 and 100
sum = 0
for i in range(0,101,2):
    print(i)
    sum = sum+i
print("Sum of Even numbers=", sum)


#7
# pyramid 1
for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=' ')
    print( )


#8
# pyramid 2
for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=' ')
    print( )



#9
# pyramid 3
count = 1
for i  in range(1,5):
    for j in range(1,i+1):
        print(count, end=' ')
        count = count+1
    print( )



#10
# pyramid 4
for row in range(1,5):
    for sp in range(1,5-row):
        print(' ', end=' ')
    for col in range(1,row+1):
        print(col, end=' ')
    for erow in range(col-1,0,-1):
        print(erow,end=' ')
    print()