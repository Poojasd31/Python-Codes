'''
OPERATOR
Solve JBK Test: Dict
'''

#Todays Agenda
#->Operator=>
#-> Arithmetic
#->Relational
#->Logical


'''PYTHON -> SYNTAX ->LOGICAL'''

#Task 1:
#Create a dict with keys and value below
# 'hi':"hello"
# 'ff':"sdfsd"
# '123':"onetwothree"
# '34':'ffff'
# once dict created print dictionary values
# and insert that values 
# in list and output should be size of list

# dict = {'hi':"hello",'ff':"sdfsd",'123':"onetwothree",'34':'ffff'}

# l=[]

# for value in dict.values():
#     l.append(value)

# print(l) #['hello', 'sdfsd', 'onetwothree', 'ffff']


# #Task 2:
# '''
# Store below data in any 
# of data structure like list, dict or combination of those
# '''
# #ind=>mh,up
# #mh=>ngp,mumbai,pune
# #up=>noida,baraili

# India={
#     "Maharashtra":["Nagpur","Mumbai","Pune"],
#     "Uttarpradesh":["Noida","Baraili"]
# }
# print(India)
# #{'Maharashtra': ['Nagpur', 'Mumbai', 'Pune'], 
# # 'Uttarpradesh': ['Noida', 'Baraili']} 


# #Task 3:
# #Can you store some list into dict show example and iterate over
# #all elements of dict and list

# dict = {
#       'Akshay Kumar':["Welcome","Hera Pheri"],
#       'Salman Khan':["Tiger","Bodyguard"]
#     }

# for i in dict.items():
#     print(i)

# for i in dict.values():
#     print(i)


# s1={11,22,33,44,55}
# s2={33,44,55,66,77}
# print(s1.difference(s2))
# #{11, 22}

# print(s2.difference(s1))
# #{66, 77}

# s1={11,22,33,44,55}
# s2={33,44,55,66,77}
# print(s1.symmetric_difference(s2)) 
# #{66, 22, 11, 77}
# print(s2.symmetric_difference(s1))
# #{66, 22, 11, 77}


# name="Welcome"
# print(name[1:6])
# #elcom

# name=input("Enter name")

# print(name[1:-1])

'''OPERATORS'''
#It is symbol which is used to perform operation on values and variables.
'''
+ = Addition Operator


'''
#LIST
# l=[11,22,33]
# m=[44,55,66]
# print(l+m) #[11, 22, 33, 44, 55, 66]
# # print(l*m) #TypeError: can't multiply sequence by non-int of type 'list'
# print(l*2) #[11, 22, 33, 11, 22, 33]


# #TUPLE
# t1=(1,2,3)
# t2=(4,5,6)
# print(t1+t2) #(1, 2, 3, 4, 5, 6)

# #DICTIONARY
# d1={1:1,2:4,3:9}
# d2={4:16,5:25}
# # print(d1+d2)
# #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# #SET
# s1={1,2,3,4,5}
# s2={4,5,22,32}
# print(s1+s2)
#TypeError: unsupported operand type(s) for +: 'set' and 'set'

'''Subtraction--> It supports Int,float and complex'''

'''Multilplication---> It supports int, float ,string
(2 strings multiplation not possible)
n1='Hello'
print(n1*hello)
##HelloHelloHello
'''
'''
DIVISION OPERATOR
'''
# n1=10
# n2=5
# print(n1/n2) #2.0 ==> Division always return float value

'''Floor Division <=> //'''
#Always return INT value
# n1=10
# n2=3
# print(n1//n2) #3

# n1=-10
# n2=3
# print(n1//n2) #-4
#It gives -4 because    => -3.333  ===> -3 and -4
#=> It always give small value

"""
POWER OPERATOR <-> **
"""
# n1=10
# print(n1**10) #10000000000

'''Modulus Operator <=> %'''
#It gives Remainder
#And Divison operator gives quotient
# n1=10
# n2=5
# print(n1%n2) #0

'''LOgical and Relational Operator'''

#Interview Question