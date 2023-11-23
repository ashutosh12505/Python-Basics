#abc = int(input('Number:'))
rev = 0
#while abc > 0:
   # ld = abc%10
   # rev = (rev*10) + ld
   # abc = abc//10
#print(rev)

a,b,c = 10, 20, 30

if a == 10 and b == 15:
    print("Matched")
else:
    print("Didn't match")

#Dictionary

# Dict ---> key:value pair

#e.g.--

dict_1 = {"name":"Ashutosh",
        "email":"abc@pqr.com","age":20,"student":True,"marks":(10, 20, 30)}
#print(dict_1)
#print(type(dict_1))

'''
values can be any data-type (even a diff dictionary).
key - a brief description of the value.
key is always in string format.
we can access any value using key.
'''

dict_2 = {"name":"RCB","type":"cricket franchise",
"name of sports":"Cricket","city":"Bengaluru",
"started participating":2008,"name of the event":"Indian Premier League",
"key players" : ["AB DE Villiers","Chris Gayle","Virat Kohli","Anil Kumble","Kevin Peterson"],
"best playing order":{"opener_1":"Chris Gayle","opener_2":"Mayank Aggarwal",
"one_down":"Virat Kohli","two_down":"AB De Villiers"}}
#print(dict_2)

#accessing key-value pair.

#print(dict_1["name"])

print("The name of the event in which rcb plays is",dict_2["name of the event"])

#print("The year in which rcb started participating in IPL is",dict_2["started participating"])
print("Key players of rcb are",dict_2["key players"])

#to access any particular value in any list present inside the dictionary.
print("I like RCB because of",dict_2["key players"][0])

#to access any key-value pair in any dictionary which is present in the main dictionary.
print("The most valuable contribution in the batting unit of rcb was given by",dict_2["best playing order"]["two_down"])

#METHODS--> 
# 
#   (1)    Get method.
#print(dict_2.get("key players"))
print(dict_2.get("best playing order"))

#   (2)      keys()

print(dict_2.keys())

#dict_keys is another data-type.It is not a list.Thats why following code doesn't work.
print(dict_2.keys)

#another way to access the keys.
for key in dict_1:
    print(key)

#Question --> If dict_2 doesn't contain "no of centuries by rcbians" key,
# then print "no centuries given".

#Solution -->

if "no of centuries by rcbians" in dict_2.keys():
    print("Centuries given")
#else:
    #print("No centuries given")

#Example-->
if "key players" in dict_2.keys():
   print("Yes it's given")
else:
   print("Not informed")

#    (3)   setdefault method.   [key,value]
dict_1 = {"name":"Ashutosh",
        "email":"abc@pqr.com","age":20,"student":True,"marks":(10, 20, 30)}

#Qstn -->If in dict_1 native state of a student is assigned, print("state given").If not, create a key called "state".
#if "state" in dict_1.keys():
    #print('state given')
#else:
    #dict_1.setdefault("state")

#print(dict_1)
for key in dict_1:
    print(key)

# By external command we can change something inside dictionary. So they are said to be mutable.

# dict_1.setdefault("state") ---- this, by default, give the value of the created key as "none".

# we can give any value to the newly created key in the same command as follows.

if "state" in dict_1.keys():
    print("state given")
else:
    dict_1.setdefault("state","Bihar")

print(dict_1)
for key in dict_1:
    print(key)

'''
     (4)   items()  ---- this gives key-value pairs in the dictionary.

returns a list containing tuple for each key-value pair.

items are a different data-types, just like keys.They aren't strings.
'''

print(dict_1.items())  #this prints key-value pairs.

print(type(dict_1.items()))  #dict_items


dict_1 = {"name":"Ashutosh",
        "email":"abc@pqr.com","age":20,"student":True,"marks":(10, 20, 30)}

#      (5)  values()  ----this gives the values,without keys


print(dict_1.values()) # for only printing items, without keys.

print(type(dict_1.values()))   #dict_values

if "state" in dict_1.keys():
    print("state given")
else:
    dict_1.setdefault("state","Bihar")

if "Bihar" in dict_1.values():
    print('Yes, state is given')
else:
    print("No, Bihar isn't present in the dictionary")


#   (6) update ----two methods.

#    first method

#dictionary_name.update({"key":"new_value"})
#for changing email from abc@pqr.com to abcd@pqr.com, following is the code
dict_1.update({"email":"abcd@pqr.com"})
print(dict_1)

#    second method
#dictionary_name["key"] = new value
dict_1["age"] = 21
print(dict_1)

#    (7) pop   ---- to remove any item (key-value pair) from the list.
dict_1.pop("email")
print(dict_1)

'''
this is used for multi-line comment.
these two lines are comments and won't be executed
'''