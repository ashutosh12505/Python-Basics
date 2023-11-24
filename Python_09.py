'''
                   SETS

Somewhat like combination of lists and tuples.
'''
#(1) These are unordered collection of unique objects. Indexing won't work here.

#unoredered.
set1 = {'this','is','a','set'}
print(set1)

#(2) As sets are collection of unique elements,repeated elements will be ignored.
set2 = {'is','english','is'} 
print(set2)

#(3) Sets are iteratable (typecasting is possible).

print(type(set2))

list1 = list(set2)
print(type(list1))

tuple1 = tuple(set2)
print(type(tuple1))

#(4) Sets are mutable, unlike tuples.
set1 = {'this','is','a','set'}

   #Methods for mutation.
'''
        Add method
  set1.add("the","first")  -- this is wrong,
   because set.add takes exactly one argument.
'''
set1.add("old")
print(set1)
#even if we run the print code for a set twice without changing anything, order of elements is different.

'''
     Difference method -- gives those elements which are unique for that set, and not in the other one.
Returns the difference in the form of a set.
Analogus to mathematics :-
setA.difference(setB) = A-B ,where A and B are sets.
'''
set3 = {"this","is","big","car","a"}
set4 = {"this","small","car","is","a"}

# to get elements which are in set3 but not in set4.
print(set3.difference(set4))   

# to get elements which are in set4 but not in set3.
print(set4.difference(set3))

'''
   Discard method.
to delete a value from the set.
set1.discard("this") --  removes "this" from set1.
'''
set5 = {"what","a","pleasant","surprise","!"}
print(set5)
set5.discard("pleasant")
print(set5)

'''
    Difference update method.
removes all those elements which are part of the another set.

set5 = {"what","a","pleasant","surprise","!"}
set6 = {"this","would","be","a","pleasant","surprise"}

set6.difference_update(set5)
print(set6)
'''
set6 = {10,20,30,40,50,60}
set7 = {10,30,50,70}

print(set7.difference_update(set6)) # returns "None",as we can't directly print without taking difference update previously.

set7.difference_update(set6) #-- converts set7 as {70}
print(set7)
'''
Now set7 has been modified as {70}. So, for any further 
commands on set7 only {70} will be considered.

For example, if we try to print set6.difference_update(set7)
then all values of set6 except {70}, if it has, will be printed.
For example-
'''


set6.difference_update(set7)
print(set6)

'''
If we want to take the original set6.difference_update(set7),
 then we will have to specify the set7 again, as follows-
'''
set7 = {10,30,50,70}
set6.difference_update(set7)
print(set6)

'''
issubset function --> returns True or False
'''
set8 = {10,15,20,25,40}
set9 = {10,20}
print(set9.issubset(set8))

#set8.add("abcd")
'''
issuperset function --> returns True of False
'''
set10 = {10,20,15,25,40,50,60}
print(set10.issuperset(set8)) # returns true because set10 is a superset of set8.
'''
on writing line no. 109, code at line no 114 returns false,
because line 109 adds the string "abcd" in set8.

 Union of sets
'''
print(set8.union(set2))