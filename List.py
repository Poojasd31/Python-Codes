#LIST
#INDEXING AND SLICING
#Data Type---> 1. Fundamental Type 2. Collective Type
#Collective DT---> List, Tuple,Set,Frozenset,dict,range


#LIST==> IT IS COMMA SEPARATED VALUES WITHIN []
#SYNTAX ==>
# var_name = [val1,val2,val3]
#Ex---> numbers = [10,20,30,40,50]

# students=["jay","Veeru","gabbar"]  
# # To check Type of variable
# print(type(students))#--> <class 'list'>

# '''List is ordered , mutable, heterogeneous collection of elements
#  where duplicates are allowed'''
# #Ordered ==> Sequence

# L = [11,22,33,44,55]
# print(L) #[11, 22, 33, 44, 55]==> It follows Sequence

# #Immutable ==> All fundamentals data type are IMMUTABLE(MEANS NON CHANGEABLE)
# #Mutable ==> Changable
#STRING========>
# course="python"
# course1=course.upper()
# print(course)
# print(course1)
# print(id(course)) # ID For Course is different 
# print(id(course1)) #ID for Course1 is Different means It is Immuatable

#LIST IS MUTABLE
#Python Memory manager (PMM)

# numbers=[11,22,33,44]
# print(id(numbers))
# numbers.append(55)
# print(numbers)  #[11, 22, 33, 44, 55]
# print(id(numbers)) #ID is same means It is mUtable

#Hererogeous = means we can store different data types of elements.
#we can store int, float,str,bool,list,etc.
 
# L=["bhushan","10.89",78,"True",False,3+8j,[1,2,3]] #HETEROGENEOUS TYPES OF ELEMENTS Because it takes diff elements inside lists
# print(L) #['bhushan', '10.89', 78, 'True', False, (3+8j), [1, 2, 3]]
# print(id(L)) #1738660303232

#Duplicates are values are allowed

# l=[11,22,33,22,11] #Duplicates are allowed it prints as it
# print(l) #[11, 22, 33, 22, 11]

#CRUD ==> {CREATE, READ , UPDATE ,DELETE}
'''Q1. How to access data from list'''
#Indexing --> To fetch single element 
#Syntax:-> var[index]
# numbers = [11,22,33,44]
# print(numbers)     #[11, 22, 33, 44]
# print(numbers[1])  #22
# print(numbers[-3]) #22

'''Q1. Create list of numbers from 11-20'''
# L=[11,12,13,14,15,16,17,18,19,20]
# #Q.2 Check type of obj
# print(type(L)) #<class 'list'>
# #Q3. Check ID
# print(id(L)) #2341299411200
# #Q4. Access 15 from List
# print(L[4]) #15
# #Q5. Print sum of 2nd pos and 5th pos
# print(L[1]+L[4]) #27

l=["raj","pavan","vijay",[11,22,33,44],"samarth"]
#Access Samarth
print(l[-1]) #samarth
#Access Vijay
print(l[2]) #vijay

print(l[-2][1])

#Slicing --> To fetch multiple element


