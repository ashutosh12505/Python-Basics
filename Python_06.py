#The previous code using logic gates.
gender = 'A'
age = 24
if age<0:
    print('Check the entered age value.')
elif gender=='M' and age>21:
    print('Yes,he can vote.')
elif gender=='M' and age<21:
    print('No,he cannot vote.')
elif gender=='F' and age>18:
    print('Yes,she can vote')
elif gender=='F' and age<18:
    print('No,she cannot vote.')
else:
    print('Enter correct value of gender.')

#Range function.
#print(range(15))

#Loops: They are used when we want to perform any operation several number of times as a repetition.\

# 1 For loop.
Ashutosh = 'abc'
for count in range(20):
    print(Ashutosh)

#Given word is printed 15 times,each in a new line.

#other example.

for count in range(10):
    print('tejas')
for pqr in range(5): #this will print from 0 to 4...means total 5 times.
    print('monk',pqr)

#format =>> for variableName in range(no of times):
#               print('what to print',variableName)

for abc in range(1,5):  #this will print from 1 to 4...means total four times.
    print('pqr',abc)

#For skippimg any mid value.
#format- for count in range(beginning, end, next-count-at)

for count in range(1,101,3):
    print('a',count)

for count in range(1,51,2):
    print(count)
    #print('Ashutosh',count)

#NEGATIVE VALUE CAN ALSO BE GIVEN.
#Formst - for xyz in range(bigger value,smaller value,next-step-at)
#              print(xyz)

#next-step-at value will always be negative in this case.

for fgh in range(16,0,-2):
    print(fgh)

# For Loop for a list.

# No need to give range,as lists maintain their own index.

teams = ['rcb','mi','csk','pbks','kkr','srh','dc','rr','lsg','gt']
for team in teams:
    print(team)   
#above command prints name of teams ,each in a new line.
    
# print(team,end="\n") --- this is the default behaviour.So,next value is coming in the new line.
# we can print next value at the same line by changing this default command.

n = input("\nEnter the value here ").split("_")
print(n) # ['2', '3']

#for example.
teams = ['rcb','mi','csk','pbks','kkr','srh','dc','rr','lsg','gt']
for team in teams:
    print(team,end=",")
    print(team,end="\n") # this is command gives same output as line no 67.
for p in range(5):
    print('abc',p)
for count in range(0,21,2):
    print("Number",end = " ")
    print(count)
# 2 WHILE Loop.

# Diff from 'for loop' is---The end of the while loop is unknown.

#format is --- while(condition):

#While loop executes commands till the condition is true.

p = 1
while p<5:
   #print(p)
   p += 1

#When we want,we can exit the loop even when the condition is true.
i = 1
while i < 6:
  #print(i)
  if i == 3:
    break
  i += 1

# Class examples.

list = [1,2,3,0,4,5]
#print("Beginning")
x = 0
while list[x] != 0:
   #print(list[x])
   x = x + 1
#print("End.")


#when the first value is the exit point from the loop.

list1 = [0,1,2,3,4,5]
#print("Beginning")
x = 0
while list1[x] != 0:
   #print(list1[x])
   x = x + 1
#print("End")

#when the last value in the list is the exit point from the list.

list = [1,2,3,4,5,0]
#print("Beginning")
x = 0
while list[x] != 0:
   #print(list[x])
   x = x + 1
#print("End")

#when there is no exit point from the loop.
#it will print till 5 as after that,index provided will be 5+1 means 6,which is out of range.

#list = [1,2,3,4,5]
#print("Beginning")
x = 0
while list[x] != 0:
   #print(list[x])
   x = x + 1
#print("End")

# INFINITE WHILE LOOP.
# while True.

list = [1,2,3,0,4,5]
#print("Beginning")
index = 0
while list[index] != 0:
   print(list[index])
   index = index + 1
#print("End.")

# Question - Write a program to reverse the number 12349298.
# Solution:

#INCORRECT:

# oak = 12349298
#for count in range(oak[8,0,-1]):
# print(oak,end="")

#CORRECT:

#STEPS 

# 1. Take the last digit from the number.
# 2. Add that digit in the reverse_number.
# 3. Remove the last digit from the number.
# 4. Do this in a loop,till the number doesn't become 0.


#Here,in the given question.
abc = 12349298
abcrev = 0

while abc>0:
    #Take the last digit from the number.
    last_digit = abc % 10                  #last_digit = 8-->9-->2-->9-->4-->3-->2-->1

    #Add that digit in the reverse_number.
    abcrev = (abcrev * 10) + last_digit    #abcrev = 8-->89-->892-->8929-->89294-->892943-->8929432-->89294321

    #Remove the last digit from the number.
    abc = abc //10                         #abc = 12349298-->1234929-->123492-->12349-->1234-->123-->12-->1-->0
print(abcrev)


#EXAMPLE

pqr = int(input('Write your number here:'))
pqr_rev = 0
while pqr>0:
    last_digit=pqr%10
    pqr_rev=(pqr_rev * 10) + last_digit
    pqr = pqr//10
print('Here is your number:',pqr_rev)