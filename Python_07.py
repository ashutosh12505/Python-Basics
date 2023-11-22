#Input function
number = input("Enter here:")
print(number)
#Input is always in the form of string.String cannot be concatenated (combined) with integer.
#Thats why following code will show error.
number = input("Enter here:")
print(number + 2)

#While the below written code works.
number = input("Enter here:")
print(number + 'abc')

#To make the code in line 7 work, typecasting can be used
# Typecasting : Converting one datatype into another datatype. 

#By default input takes the datatype str.
# It means: number = str(input("Upload here:")) ==== number = input("upload here:")

#For example:To give an input in terminal we will convert the input given here in that same type,in this case which is int.
number = int(input("Upload here:"))
print(number + 6)

#number = float(input("Upload here:"))
#print(number + 6)

#TUPLES.

#lists - square brackets.
#tuples - round brackets.

list1 = [1,2,3,4,5]
#print(list1)
#print(type(list1))
#print(list1[2])
#can append/insert/delete elements.
#print(len(list1))

tuple1 = (10,20,30,40,50)
#print(tuple1)
#print(type(tuple1))
#print(tuple1[2])
#cannot append/insert/delete elements.
#print(len(tuple1)) can measure length in the same way.

#  Lists are mutable, tuples are inmutable.
#  i.e. we can change any element in list by writing external program, but that isn't possible for tuples.

#multiple datatypes can be put and printed.
tuple2 = (1,2+3j,"abc",True)
#print(tuple2)

#repeated values are considered different.
tuple3 = (100,200,100,300,100,500,True,5+2j)
#print(tuple3)

#while giving only one element in a tuple, put a comma in the end.otherwise it will become the type of that element,not a tuple.
tuple4 = (12)      #int
tuple5 = (12,)     #tuple
tuple6 = ("abc")   #str
tuple7 = ("abc",)  #tuple

#print(type(tuple4))
#print(type(tuple5))
#print(type(tuple6))
#print(type(tuple7))

abc = tuple(('a','b','c','d'))
#print(abc)
#print(type(abc))

#Operations on tuple.

# 1 Tuple concatanation.

a = ('v1','v2','v3')
b = ('v4','v5')
pqr = a + b

#print(pqr)
#print(type(pqr))

# 2 Tuple nesting.

ntuple = ((10,20,30,40,50),(1,2+3j,"abc",True),('a','b','c','d'),('v1','v2','v3'),('v4','v5'))
#print(type(ntuple))

a = ('v1','v2','v3')
b = ('v4','v5')

op = (a,b)
#print(op)

# 3 Repetitive tuple.

#ab = ('tejas') * 15 --- gives tejastejastejas.....15 times
ab = ('tejas',) * 15
#print(ab)

# 4 Deleting a tuple.
pq = ('A',) * 10
#print(pq)
del pq # after writing this, error will be shown on executing stating that no such file exists.
#print(pq) 

# 5 Converting a list into a tuple.

#format--  new_tuple = tuple(the_list)
initial_list = ['1','2','3','4','5']
final_tuple = tuple(initial_list)

print(initial_list)
print(type(initial_list))

print(final_tuple)
print(type(final_tuple))

# 6 Converting a tuple in a list.

#similar to the opposite conversion
initial_tuple = (5,10,'Python',True,5+6j)
print(initial_tuple)
print(type(initial_tuple))

final_list = list(initial_tuple)
print(final_list)
print(type(final_list))