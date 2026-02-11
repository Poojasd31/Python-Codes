#DATA Types
#SET AND their Methods

'''Set has a comma separated value within curly braces
It is unoredered
Collection of immutable elements
'''

#How to add data?
# add()
# var.method()
'''Syntax: var.add(value)'''

# s={11,22,33,44}
# s.add(66)
# print(s) #{33, 66, 11, 44, 22}

# #HOW TO DELETE DATA FROM SET?
# #by using pop(), remove() and discard(), clear()
# #--->
# ##REMOVE() Method
# '''Syntax: var.remove(value)'''
s={11,22,33,44}
s.remove(11)
print(s) #{33, 44, 22}
#Remove method gives value in return 'NONE'

# #POP() Method
# '''syntax: var.pop()'''
s={11,22,33,44}
s.pop() # It deletes value randomly
print(s) #{11, 44, 22}
print(s.pop()) #it give deleted value in return

# #discard()
# '''
# var.remove(value)
# var.discard(value)
# '''
# s={11,22,33,44}
# s.discard(11)
# print(s) #{33, 44, 22}
# # s.remove(111)
# # print(s)
# # print("coding") #KeyError: 111

# s.discard(111)
# print(s)
# print("coding")
#{33, 44, 22}
#coding
'''
remove deletes value if present otherwise give error
discard deletes value if present otherwise run whole code
'''

#del

# s={11,22,33,44}
# del print(s) #SyntaxError: cannot delete function call

#INTERSECTION() 
'''Return the intersection of two sets as a new set.
(i.e. all elements that are in both sets.)'''

# s1={11,22,33,44}
# s2={33,44,55,66}
# s=s1.intersection(s2) #it will return new set
# print(s)  #{33, 44}

# # difference()
# '''Return the difference of two or more sets as a new set.

# (i.e. all elements that are in this set but not the others.)'''
# s=s1.difference(s2)
# print(s) #{11, 22}
# s=s2.difference(s1)
# print(s) #{66, 55}

#Intersection_update()-->
''' 
(method) def intersection_update(*s: Iterable[Any]) -> None
Update a set with the intersection of itself and another.
'''
# s1={11,22,33,44}
# s2={33,44,55,66}
# s1.intersection_update(s2)
# print(s1) #{33, 44}
# print(s2) #{33, 66, 44, 55}
'''
intersection it will not update s1 and s2
but in case of intersection_udate it will update the value of s1
'''

#difference_update()
'''
(method) def difference_update(*s: Iterable[Any]) -> None
Remove all elements of another set from this set.
'''
# s1={11,22,33,44}
# s2={33,44,55,66}
# s1.difference_update(s2)
# print(s1) #{22, 11}
# s2.difference_update(s1)
# print(s2) #{66, 55}

# s1={11,22,33,44}
# print(type(s1)) #<class 'set'>
'''(function) def dir(
    o: object = ...,
    /
) -> list[str]
Show attributes of an object.'''
# print(dir(s1)) 
#['__and__', '__class__', '__class_getitem__', '__contains__', 
# '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', 
# '__ge__'
# , '__getattribute__', '__getstate__', '__gt__', '__hash__', 
# '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', 
# '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', 
# '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', 
# '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', 
# '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard',
#  'intersection', 'intersection_update', 'isdisjoint', 'issubset', 
# 'issuperset', 'pop', 'remove', 
# 'symmetric_difference', 'symmetric_difference_update', 'union',
#  'update']


'''LIST'''
# l=[11,22,33,44]
# l.append(55)
# print(l) #[11, 22, 33, 44, 55]
# l.append(33)
# print(l) #[11, 22, 33, 44, 55, 33]

# s={11,22,33,44}
# '''() -> set[int]
# Return a shallow copy of a set.
# '''
# s1=s.copy()
# print(s1) #{33, 11, 44, 22}

#issubset() Method
'''(method) def issubset(
    s: Iterable[Any],
    /
) -> bool
Test whether every element in the set is in other.'''
'''Check whether s2's every element in s1'''
# s1={11,22,33,44}
# s2={33,44,55,66}
# print(s1.issubset(s2)) #False

# s3={11,22,33,44}
# s4={11,22}
# print(s3.issubset(s4))#False
# print(s4.issubset(s3))#True

#issuperset()
'''
(method) def issuperset(
    s: Iterable[Any],
    /
) -> bool
Test whether every element in other is in the set.

'''
s1={11,22,33,44}
s2={11,22}
l2=[11,22]
print(s1.issuperset(s2)) #True
print(s1.issuperset(l2)) #True
print(s2.issuperset(s1)) #False




#symmetric_difference
'''symmetric_difference()
symmetric_difference" is not definedPylancereportUndefinedVariable
(function) symmetric_difference: Any
'''
s1={11,22,33,44}
s2={33,44,55,66}
print(s1.symmetric_difference(s2)) #{66, 11, 22, 55}
print(s1.difference(s2)) #{11, 22}

# #symmetric_difference_update()
'''symmetric_difference_update()
 (function) symmetric_difference_update: Any
'''
s1={11,22,33,44}
s2={33,44,55,66}
s1.symmetric_difference_update(s2)
print(s1) #{66, 11, 22, 55}
print(s2) #{33, 66, 44, 55}

# #isdisjoint
# '''
# isdisjoint():
# "isdisjoint" is not defined
# (function) isdisjoint: Any
# '''
# s1={11,22,33,44}
# s2={33,44,55,66}
# print(s1.isdisjoint(s2)) #False

#union()
s1={11,22,33,44}
s2={33,44,55,66}
s=s1.union(s2)
'''Return the union of sets as a new set.

(i.e. all elements that are in either set.)'''
print(s) #{33, 66, 11, 44, 22, 55}


##INTERVIEW QUESTIONS
"""
1. WHAT IS SET?
2. WHAT ARE METHODS OF SET?
3. WHAT IS DIFF BETWEEN REMOVE AND POP
4.              BETWEEN DISCARD AND Remove
"""