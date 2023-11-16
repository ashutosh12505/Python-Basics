# STRING SLICING ---- output is in the form of a list.

word = "abcde fghij klmno pqrst uvwxy z"
print(word[1:3])
#print(word[0:30])
#print(word[0:32])
#print(word[0:50])
print(word[0:])
#--print(word[12:1]) ---- This isn't working because between [here] we have to start from smaller number and go till larger number.
#print(word[-10:-2])
#--print(word[-1:-100]) ---- This isn't giving any output..only blank space because we should start from smaller number [here].
print(word[-12:-1])
#--print(word[-12:-0]) ---- Not working because there isn't any index as {-0}

#correct method is to leave the last value...only give the beginning point.

#print(word[-12:])
print(word[:10])

# Lists
#creating list using []
exam = ['a','b','c','d','e','f','g','h','i','j','k','l']
#print(exam)
#print(type(exam))

#creating list using list constructor
#incorrrect
#quad = list[]
#correct---
quad = list()
print(quad)
#print(type(quad))

#separates each letter
ipec = list("Ashutosh kumar singh")
print(ipec) # ['A', 's', 'h', 'u', 't', 'o', 's', 'h', ' ', 'k', 'u', 'm', 'a', 'r', ' ', 's', 'i', 'n', 'g', 'h']
print(len(ipec)) #space is also counted

#different data-types can be placed in a single list

#below is class tuple >>
tejas = (100,"Ashutosh",True,4+5j)
#print(tejas)
#print(type(tejas))


#below is class list >>
squad = [100,"Ashutosh",True,4+5j]
#print(squad)
#print(type(squad))

#list is managed by indices
ipec = list("Ashutosh kumar singh")
#print(ipec[7])
print(ipec[-3])

#print(ipec[0:8])

#print(ipec[0])
#print(ipec[1])
#print(ipec[2])
#print(ipec[3])
#print(ipec[4])
#print(ipec[5])
#print(ipec[6])
#print(ipec[7])

#2-D lists.
group = [(1,2,3),(4,5,6),(7,8,9)]
print(group) # [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(type(group))
print(group[1]) # (4, 5, 6)
print(group[0:]) # [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(group[1][2])

#REPLACEMENT MECHANISMS IN LISTS.

group[0] = [100]
group[1] = (50)
group[2] = ['500']
print(group)

kalyani = ['a','b','c','d','e','f']
# kalyani[0:3] = [10,11,12]
# kalyani[3:5] = (1,2,3,4) # ['a', 'b', 'c', 1, 2, 3, 4, 'f']
# kalyani[2] = (3)
kalyani[3:9] = 1,2 # ['a', 'b', 'c', 1, 2]
print(kalyani)