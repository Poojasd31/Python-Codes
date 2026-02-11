'''Data Type=>
   >TUPLE

LIST: Mutable, Heterogeneous and duplicates
1.access : var[index], var[si:ei:sv]
Every Element has two index POSITIVE AND NEGATIVE
*how to add data:
l=[11,22,33,44,66]
Method
var=value
var.method()
l.append(77)---->Add element at last
l.insert(4,55)--->add at index
l=[11,[22,33,44],66]
l[1].append(999)
l[1].insert(1,222)

HOW TO REMOVE DATA===>
l=[11,[22,33,44],66]
l.remove(11)
l[1].remove(22)

l=[11,22,33,44,22,55]
l.pop(-2)

HOW TO UPDATE
var[index]=value
l[2]=333 --> To Update

l=[11,22,33]
m=[1,2,3,4]
add content of m to l

l.extend(m)
print(l) #[11, 22, 33, 1, 2, 3, 4]

*Append==> Append object at the end of list
*Extend==> Extend list by add element of list to another list

'''
##### TUPLE #####
'''Tuple is a comma separated values within ()(parantheses)'''
'''Ordered, immutable, heterogeous collection of elements where duplicates are 
 allowed'''
#Ordered: It follows particular Sequence
#immutable:  we cannot update , add, delete in tuple 
#Heterogeous collection of element
#Tuples have ordered element
#t=(11,22,33,22,11)
#Syntax: 
''' var = (v1,v2,v3,.....)'''

# numbers=(10,20,30,40)
# print(type(numbers)) #<class 'tuple'>  ----> To check data type of variable

# # -5   -4 -3 -2 -1  -->Negative / Reverse Indexing
# t=(11,22,33,44,55)
# #  0   1  2  3  4   --> Positive / Forward Indexing

# #By using Indexing and Slicing
# '''Indexing'''
# print(t[2]) #33
# print(t[-3]) #33
# print(t[0]) #11
# print(t[-1]) #55

# '''Slicing-> To fetch multiple elements'''
# print(t[0:5:1]) #(11, 22, 33, 44, 55)
# print(t[0:4:1]) #(11, 22, 33, 44)
# print(t[-2:0:-1]) #(44, 33, 22)
# print(t[1:-1:1]) #(22, 33, 44)

'''Start Index'''
# t=(11,22,33,44,55,66)
# print(t[0:3:1]) #(11, 22, 33)
# print(t[:3:1])  #(11, 22, 33)
'''Default value 0 in case of forward'''
# print(t[-1:-4:-1]) #(66, 55, 44)
# print(t[:-4:-1]) #(66, 55, 44)
'''Default value -1 in case of reverse'''

'''END INDEX'''
# t=(11,22,33,44,55,66)
# print(t[-3:6:1]) #(44, 55, 66)
# print(t[-3::1]) #(44, 55, 66)
'''Default value jitani length di hui hai utani hi hoti hai'''
# print(t[-4:-7:-1]) #(33, 22, 11)
# print(t[-4::-1])   #(33, 22, 11)

'''STEP VALUE'''
# t=(11,22,33,44,55,66)
# print(t[1:4:1]) #(22, 33, 44)
# print(t[1:4]) #(22, 33, 44)
# '''step value by default is 1'''

# print(t[0:-1]) #(11, 22, 33, 44, 55)
# print(t[0:-1:2]) #(11, 33, 55)

#  0   1  2   3                             4  5  6
t=(11,22,33,[111,222,333,(1,2,3,4),444,555],44,55,66)
#   -7 -6 -5   -4                            -3 -2 -1

print(t[:3:]) #(11, 22, 33)

print(t[-3::]) #(44, 55, 66)
# 111 222
print(t[3][:2:])  #[111, 222]

#444 555
print(t[3][-2::]) #[444, 555]

#3,2,1
print(t[3][3][-2::-1]) #(3, 2, 1)

"""I Ques"""
"""what is Tuple
what is indexing
what is slicing"""