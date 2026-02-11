'''SET'''

# t=("rajesh")
# print(type(t)) #<class 'str'>
# #It will not consider ()

# num=(10,20)
# print(type(num))

# #Q....How to cretae Tuple with single value
# #===>

# t1=("Pooja",)
# print(type(t1)) #<class 'tuple'>

'''SET'''
#IT IS COMMA SEPARATED ELEMENT WITHING {}
#SYNTAX:
#var={v1,v2,v3,......}

s={11,22,33,44}
print(type(s)) #<class 'set'>

'''SET IS 
UNORDERED,

MUTABLE
AND HETEROGENEUOS COLLECTION OF IMMUTABLE ELEMENTS
WHERE DUPLICATES ARE NOT ALLOWED'''

#UNORDERED --> that's why index is not there
print(s) #{33, 11, 44, 22}

#MUTABLE -->
s.add(55)
print(s) #{33, 11, 44, 22, 55}
#if it is mutable we can add data, delete data from set 
#but we cannot update data because It doesn't have index

#HETEROGENEOUS COLLECTION OF IMMUTABLE ELEMENT
s1={10,10.89,'vaibhav',True,4+7j,(11,22,33)}
print(type(s1)) #<class 'set'>
print(s1) #{True, (11, 22, 33), 10.89, 'vaibhav', (4+7j), 10}
# s2={10,10.89,'vaibhav',True,4+7j,(11,22,33),[1,2,3]}
# print(s2) #unhashable type: 'list'
'''It is getting error because
Set is collection of Immutable elements and list is mutable'''

# #NO nested set
# s2={10,10.89,'vaibhav',True,4+7j,(11,22,33),{1,2}}
# print(s2) #unhashable type: 'set'

#Duplicates are not allowed not giving error but it gives values one time
s={11,22,33,11,33,44,55,66}
print(s) #{33, 66, 22, 55, 11, 44}

l=[]
print(type(l)) #<class 'list'>

t=()
print(type(t)) #<class 'tuple'>

s=""
print(type(s)) #<class 'str'>

se={}
print(type(se)) #<class 'dict'>

'''{}
It is used for set and dict'''

#How to represent empty set
#==>
'''
class XYZ:
   pass

   
#object of class
# x=XYZ()  

class list:
   pass
   
l1=list()
l=[]

class tuple:
   pass
   
t=()
t=tuple()

class set:
   pass
   
s=set()
'''

s3={11,22,33}
print(type(s3)) #<class 'set'>

s4=set()
print(type(s4)) #<class 'set'>

'''class set()
set() -> new empty set object
set(iterable) -> new set object

Build an unordered collection of unique elements.'''

# s=set([11,22,33,44])
# print(type(s)) #<class 'set'>
# print(s) #{33, 11, 44, 22}

# s=set([11,22,33,[1,2,3]])
# print(s) # unhashable type: 'list'

l={11,22,33,22,33,55}
print(len(l)) #4

t=(11,)
print(t) #(11,)
print(type(t)) #<class 'tuple'>