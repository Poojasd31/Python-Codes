"""
Today's Agenda:->
........................
For Loop 
While Loop
   
"""
# IF ELIF ELSE STATEMENT
'''
if cond:
 statement
elif cond:
 statement
else:
  statement
'''

# num = 10
# if num>5:
#     print("hello")
# if num>7:
#     print('welcome')
#hello
# welcome

# num = 10
# if num>5:
#     print("hello")
# if num>7:
#     print('welcome')

# num=10
# if num>5:
#     if num>11:
#         print("hello")
#     else:
#         print("welcome")
#welcome

'''Iterative statements'''#It helps us to do iteration
#for loop
#while loop
"""Both are using for iteration"""

#FOR LOOP
#syntax:
"""for temp_var in iterable:
      #body for loop
      # statements
"""
# for and in =>keyword


# l=[11,22,33,44,55] #iterable
# for num in l:
#     print(num)

# 11
# 22
# 33
# 44
# 55

#wap to print numbers from 11-20

# for num in range(11,21):
#     print(num)

#11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 13
# 14
# 15
# 16
# 13
# 14
# 15
# 13
# 14
# 13
# 14
# 13
# 14
# 13
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20

#Even number from 11-20

# for num in range(11,21):
#     if num%2==0:
#         print(num)
# 12
# 14
# 16
# 18
# 20

#WAP TO CHECK STRING IS PALINDROME OR Not

# name = str(input("Enter name=>"))

# if (name==name[::-1]):
#     print("Palindrome")

# else:
#     print("Not Palindrome")

#Enter name=>WOW
# Palindrome



#WAP to print sum of all numbers
# l=[1,2,3,4,5]

# sum=0

# for num in l:
#     sum+=num

# print(sum)
#15

#WAP to print Multiplication of all numbers

# l=[1,2,3,4]

# mul=1

# for num in l:
#     mul*=num
# print(mul)
#24

# n1="hello"
# n2="welcome"
# print(n1+n2)
#hellowelcome

#WAP to check string is palindrome or not
#  without using slicing

# string=input("Enter name=>")

# rev=''

# for char in string:
#     rev=char+rev

# if string==rev:
#     print('palindrome')
# else:
#     print("Not Palindrome")

#Enter name=>MADAM 
# palindrome

# l=[11,22,33,44,55]

# l_rev=[]

# for num in l:
#     l_rev=l_rev+l

# print(l_rev)

#WAP TO check number is perfect or not

#6=1,2,3 divide hoto and tyachi addition => 1+2+3=>6
#and number 2 same ahet so It is perfect number


# num=int(input("Enter num:=>"))
# sum=0
# for i in range(1,num):
#     if num%i==0:
#       sum=sum+i

# print("Sum",sum)

# if num==sum:
#    print("Perfect Number")
# else:
#    print("Not Perfect Number")
# '''
# Enter num:=>28
# 28
# Perfect Number
# '''

# dict = {'a': 1, 'b': 2, 'c': 3}
# for i in dict.values():
#   print(i)

 #Output
# 1
# 2
# 3

#Q.3 WAP to print sum of all even numbers from 1 to 30.

sum = 0
for num in range(1,31):
    if num%2==0:
        sum=sum+num

print(sum)
#240