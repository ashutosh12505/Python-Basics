# Bitwise operators = & (and) , | (or) , ~ (not) , ^ (xor)
a, b = 5, 4

'''
4 = 0100
5 = 0101

AND = 0100      = 4
OR = 0101       = 5
NOT (a) = 0101  = -(0101 + 1) = -0110 = -(4+2) = -6  (1 carrried, 0 remained at unit place)
XOR = 0001      = 1
'''

print("Bitwise AND is :" ,a & b)
print("Bitwise OR is :" ,a | b)
print("Bitwise NOT of a is :" ,~a)
print("Bitwise xor is :" ,a ^ b)


x = 4         #100
y = 2         # 10
print(x | y)  #110 = 6


#Functions -- A way to create some re-usable block of codes, which can be called anytime for processing.
# syntax -- def function_name(parameters):

# Creating a function to add two numbers

def add(x, y):
    print(x + y)

add(2,3)
add(4,10)
add(2,30)
add(20,3)

# To get two numbers and print the cube of the sum.

def pqr(x, y):
    return x + y   # here 'add' function is defined.

p = int(input("Enter the first number :"))
q = int(input("Enter the second number :"))

sv = pqr(p, q)
print(sv*sv*sv)
print(sv**3)

# Not of a negative number is positive
a = 5
b = -5 
print(~a)  # -(101 + 1) = -110 = -6
print(~b) # -101 + 1 = -(-100 )= 4

# to find ~ of any number, add 1 and reverse the sign.


# Input Output Formatting.
name = "Ashutosh"
age = 20

#print("My name is "+name+" and I am "+ age + " years old")    #invalid syntax

#print("My name is",name,"and I am",age,"years old")   #correct syntax

# formatting
print(f"My name is {name} and I am {age} years old") #no need of typecasting

abc = ("Price is only {price:.2f} rupees")
print(abc) #the whole string gets printed even if price is defined.
price = 25
print(f"Price is only {price} rupees")  #works completely fine.

abc = "Price is only {price:.2f} rupees"
print(abc.format(price = 30))

txt = "For only {price:.9f} dollars!"
print(txt.format(price = 49))

abc = "For only {price:.4f} dollars".format(price = 10)
print(abc)

pqr = "For only {price} rupees".format(price = 25)
print(pqr)  # prints absolute value

# Date-time

import datetime
print(datetime.datetime.now()) #gives year-month-date  hour-minute-second-micro_second
print(datetime.datetime.now().strftime("%a")) #weekday - full version e.g. wed
print(datetime.datetime.now().strftime("%A")) #weekday, full version e.g. wednesday
print(datetime.datetime.now().strftime("%w")) #weekday as a number, sunday is 0
print(datetime.datetime.now().strftime("%d")) #date of month
print(datetime.datetime.now().strftime("%b")) #month name, short version e.g. dec
print(datetime.datetime.now().strftime("%B")) #month name, full version e.g. december
print(datetime.datetime.now().strftime("%m")) #month as a number -- 01-12
print(datetime.datetime.now().strftime("%y")) #year without century e.g. 22
print(datetime.datetime.now().strftime("%Y")) #year with century e.g. 2022
print(datetime.datetime.now().strftime("%H")) #hour 00-23
print(datetime.datetime.now().strftime("%I")) #hour 00-12
print(datetime.datetime.now().strftime("%p")) #AM/PM
print(datetime.datetime.now().strftime("%M")) #minute 00-59
print(datetime.datetime.now().strftime("%S")) #second 00-59
print(datetime.datetime.now().strftime("%f")) #microsecond 000000-999999
print(datetime.datetime.now().strftime("%z")) #UTC offset
print(datetime.datetime.now().strftime("%Z")) #Timezone
print(datetime.datetime.now().strftime("%j")) #day no of the year ... 001-366
print(datetime.datetime.now().strftime("%U")) #week number of the year, sunday as the first day of week...00-53
print(datetime.datetime.now().strftime("%W")) #week number of the year, monday as the first day of the week...00-53
print(datetime.datetime.now().strftime("%c")) # Local version of date and time
print(datetime.datetime.now().strftime("%C")) # century e.g. 20
print(datetime.datetime.now().strftime("%x")) # local version of date
print(datetime.datetime.now().strftime("%X")) #local version of time
print(datetime.datetime.now().strftime("%%")) # A % character


z = datetime.datetime(2002, 9, 30)
print(z.strftime("%B"))
print(z.strftime("%j"))

#creating a variable and using datetime
date = datetime.datetime.now().strftime("%d")
day = datetime.datetime.now().strftime("%A")
month = datetime.datetime.now().strftime("%B")
year = datetime.datetime.now().strftime("%Y")

print("Today's date is",str(date),",day is",day,"and the month and year are",month,",",str(year),"respectively.") #typecasting used.

time = datetime.datetime.now().strftime("%X")
am_pm = datetime.datetime.now().strftime("%p")

print(f"Today is {date}th of the month {month} of the year {year} and the time is {time} {am_pm}")

local_date = datetime.datetime.now().strftime("%x")

print("Simply, the time is",time,am_pm)
print("Simply, the date is",local_date)

# to print the name of month by taking any input integer from the user


#by making tuple
month = ("January","February","March","April","May","June","July","August","September","October","November","December")

num = int(input("Enter the month number here: "))
print(month[num - 1])

#by making list
m_list = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}

user_input = int(input("Enter the month number here: "))
print(m_list[user_input])

#by taking inputs and printing date using datetime

date = int(input("Enter date here [01-31] : "))
month = int(input("Enter month here [01-12] : "))
year = int(input("Enter in the form [yyyy] : "))

import datetime
the_date = datetime.datetime(year, month, date)
print(the_date)