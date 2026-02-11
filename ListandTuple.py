'''List and Tuple '''
#tuple
'''t=(11,22,33,44)'''
#Tuple is immutable
#every element has two index

# t=(11,22,33,44)
# print(type(t)) #<class 'tuple'>

# t1= 11,22 ,33,44
# print(type(t1)) #<class 'tuple'>

# l=[11,22,33]
# print(type(l)) #<class 'list'>

# l1=11,22,33
# print(type(l1)) #<class 'tuple'>

#LIST
'''
List
1. List is comma separated values within []
2. It Mutable
3. [] is mandatory
for ex-
l=[11,22,33] but we cannot write list without [] it shows us as Tuple
4.List supports unpacking
5. List requires large memory as compared to tuple
6. Speed: List is slow
7. List is not memory efficient
8.If data is not fixed used LIST
For Ex. If student count going to change then use List
'''

#Tuple
'''
Tuple
1. Comma separated values within()
2. it is immutable
3. () is not mandatory
for ex-
t=(11,22,33) or t=11,22,33
4. Tuple supports packing and unpacking
5. It requires less memory
6. Speed: Tuple is fast
7. Tuple is more efficient as compared to List because it points same memory in case if data is same
8. 

'''


#Tuple
# t=(11,22,33)
# a,b,c=t  #whre a=11,b=22,c=33
# print(a)
# print(b)
# print(c)
# #It is called unpacking

# n1=100
# n2=200
# n3=300
# t=n1,n2,n3
# print(t) #(100, 200, 300)
#It called packing

# #List
# l=[11,22,33]
# a,b,c=l
# print(a) #11
# print(b) #22
# print(c) #33

# n1=10
# n2=20
# l=n1,n2
# print(l)  #(10, 20)
# #It shows that it is not supporting packing

#import
'''Import keyword help us import module or file'''
#Syntax
'''import module-name'''
'''module-name.var'''
#import p1
#print(p1.num)
#print(p1.l)

from sys import getsizeof
numbers=[10,20,30]
print(getsizeof(numbers)) #88



#Second Syntax for import
'''
from modulename import function/class/var
for ex.. from p1 import num,l 
print(num)
print(l)
'''
from sys import getsizeof
numbers=(10,20,30)
print(getsizeof(numbers)) #64

#getsizeof()==>to get size of tuple and list

L=[11,22,33,44]
L1=[11,22,33,44]
print(id(L)) #1990791059712
print(id(L1)) #1990791057792

num1=100
num2=100
print(id(num1)) #140705414710808
print(id(num2)) #140705414710808

t1=(11,22,33)
t2=(11,22,33)
print(id(t1)) #2057719057408
print(id(t2)) #2057719057408

name="Pooja"
print(id(name)) #1695800954768
name1="Pooja"
print(id(name1)) #1695800954768

#String points same memory location in case of same data

#MODULE IS PYATHON FILE WHICH CONTAINS FUNCTION , CLASS AND VARIABLE