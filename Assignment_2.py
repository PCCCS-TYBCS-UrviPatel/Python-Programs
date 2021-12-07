#***Solved Programs***
#2.1
print("use of len(), min() and max()")
msg = "Hoopla"
print(msg)
msg2 = 'He said,\'Let Us Python\''
file1 = 'C:\\temp\\newfile'
file2 = r'C:\temp\newfile'
print(msg2)
print(file1)
print(file2)
msg3 = 'What is this life if full of care...\
    We have no time to stand and stare'
msg4 = """What is this life if full of care...
We have no time to stand and stare
"""
msg5 = ('What is this life if full of care...\
    We have no time to stand and stare')
print(msg3)
print(msg4)
print(msg5)
msg6 = 'MacLearn!!'
print(msg*3)
msg7 = 'Utopia'
msg8 = "Today!!!"
msg7 = msg7+msg8
print(msg7)
print(len(msg))
print(min(msg))
print(max(msg))


#2.2
print("Operations on string 'Bamboozled'")
s = 'Bamboozled'
print(s[0], s[1])
print(s[-10],s[-9])
print(s[8],s[9])
print(s[-2],s[-1])
print(s[2:10])
print(s[2: ])
print(s[-8:])
print(s[0:6])
print(s[ :6])
print(s[-10: -4])
print(s[:4])
print(s[::-1])
print(s[0:10:1])
print(s[0:10:2])
print(s[0:10:3])
print(s[0:10:4])
s = s+' Hype!'
print(s)
s = s[:6]+' Monger'+s[-1]
print(s)

#2.3
print("Operation on Strings")
s1 = 'NitiAayog'
s2 = 'And Quiet Flows The Don'
s3 = '1234567890'
s4 = 'Make $1000 a day'
print('s1= ', s1)
print('s2= ', s2)
print('s3= ', s3)
print('s4= ', s4)
print('Check isalpha on s1,s2')
print(s1.isalpha())
print(s2.isalpha())

print('Check isdigit on s3,s4')
print(s3.isdigit())
print(s4.isdigit())

print('Check isalnum on s1,s2,s3,s4')
print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
print(s4.isalnum())

print('Check islower on s1,s2')
print(s1.islower())
print(s2.islower())

print('Check isupper on s1,s2')
print(s1.isupper())
print(s2.isupper())

print('Check startswith and endswith on s2')
print(s2.startswith('And'))
print(s2.endswith('And'))


#2.4
s1 = "Bring It On"
print(s1.upper())
print(s1.capitalize())
print(s1.title())
print(s1.swapcase())

print(s1.find('I'))
print(s1.find('On'))
print(s1.replace('It', 'Him'))

s2 = " Flanked by spaces on the either sides "
print(s2.lstrip())
print(s2.rstrip())

s3 = 'C:\\Users\\Kanetkar\\Documents'
print(s3.split('\\'))
print(s3.partition('\\'))


#2.5
s = "The Trrible Tiger Tore The Towel"
pos = s.find('T', 0)
print(pos, s[pos])
pos = s.find('T', pos+1)
print(pos, s[pos])
pos = s.find('T', pos+1)
print(pos, s[pos])
pos = s.find('T', pos+1)
print(pos, s[pos])
pos = s.find('T', pos+1)
print(pos, s[pos])
pos = s.find('T', pos+1)
print(pos, s[pos])
pos = s.find('T', pos+1)
print(pos, s[pos])
c = s.count('T')
s = s.replace('T','t',c)
print(s)


#**Unsolved Programs**
#2.2.1
# Extract string subparts
s = 'Shenanigan'
print(s[0],s[1])
print(s[4],s[5])
print(s[2:])
print(s[:6])
print(s[:-4])
print(s[-10:-4])
print(s[0:6])
print(s[:])
print(s[0:10:2])
print(s[0:10:3])
print(s[0:10:4])
s = 'Shenanigin'
g = 'Type'
a = s+g
print(a)
s = 'Shenanigin'
t = 'Wabbite'
b = s[:6]+t
print(b)


#2.2.2
#Capitalizing each word
s = 'an inferior lawyer with dubious practices'
t = ''
for w in s.split():
    t = t+w.capitalize()+' '
print(t)


#2.2.3
# Search and replace string
msg = "Light travels faster than sound. This is why some people appear bright until you hear them speak"
newmsg = msg.replace('Light','LIGHT').replace('sound','SOUND')
print(newmsg)


#2.2.4
s = 'HumptyDumpty'
print('s=',s)
print(s.isalpha())
print(s.isdigit())
print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.startswith('Hump'))
print(s.endswith('Dump'))


#2.2.5
msg = 'The difference between stupidity and genius is that genius has its limits'
for word in msg.split():
    for word in msg.split():
        print(word)