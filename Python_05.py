#conditional statements.
#Logic gates - AND,OR,NOT

#AND gate
#F F   False
#F T   False
#T F   False
#T T   True

#OR gate
#T F  True
#T T  True
#F T  True
#F F  False

#NOT gate
#F  True
#T  False

#if (8<10):
    #print('Yes 8 is less than 10')
#else:
    #print('NO 8 is not less than 10')

#USE "and" IF MORE THAN ONE STATEMENTS HAVE TO BE CHECKED.

#if (8<10 and 10<15):
    #print('Yes 8 is less than 10')
#else:
    #print('NO 8 is not less than 10')

#when connected by "and",if any condition is wrong then whole condition becomes wrong.
if (8<10 and 10>12):
    print('Yes 8 is less than 10')
else:
    print('NO 8 is not less than 10')

#when connected by "or",if any condition is wrong then also the code works.
if (8<10 or 10>20):
    print('Yes 8 is less than 10')
else:
    print('NO 8 is not less than 10')

    #NOT Gate Example.
abc = True
xyz = not(abc)

#print(abc)
#print(xyz)

game = False
cricket = not(game)

#print(game)
#print(cricket)

# Example question
gender = 'A'
age = 15
if age<0:
    print('Please enter the correct value of age')
elif gender =='M':
    if age>21:
        print('He can vote')
    else:
        print('He cannot vote')
elif gender =='F':
    if age>18:
        print('Yes,she can vote') 
    else:
        print('No,she cannot vote')
else:
    print('Please enter the correct value of gender')