# n1=10
# n2=20

# # n1=n2
# # n2=n1
# # print(n1) #20
# # print(n2) #20


# n1,n2=n2,n1
# print(n1) #20
# print(n2) #10

'''FLOW CONTROL STATEMENTS'''
#"In python one line means one statement"

"""
Types:
1.Conditional Statements
=> If statement
=>if else statement
=>if elif else statement

2.Iterative statements
=>for loop
=>while loop

3.Transfer statements
=>pass
=>continue
=>break

"""

# print("Hello")
# print("Welcome")
#Hello
#Welcome
#Python executes line by line

'''IF STATEMENT'''
#Syntax:
"""
if condition:
  #body
  #statement

if => Keyword
condition => Output always in boolean form either True/False
: => Colon
space=> Indentation(4 Space, 1 tab)

"""
# age=eval(input('Enter Age:'))
# if age>18:
#     print("You are Eligible")
# print("Thank You")
# '''
# Output:
#    You are Eligible
#    Thank You'''

# num = eval(input("Enter Number:=>"))
# if num > 5:
#     print("Number is Greater than 5")
# #Number is Greater than 5

# #WAP to iterate positive numbers from list
# l=[-11,22,-33,44,-55,66,-77]

# for num in l:
#     if num>=0:
#         print(num)
# #22
# #44
# #66

#WAP TO PRINT NUMBERS BETWEEN 10-20 FROM GIVEN LIST

# L=[1,4,5,11,14,17,19,24,67,89,90]

# for num in L:
#     if (num>=10 and num<=20):
#         print(num)

#11
#14
#17
#19


# #which is divisible by 2

# L=[1,4,5,11,14,17,19,24,67,89,90]

# for num in L:
#     if num%2==0:
#         print(num)
# '''4
# 14
# 24
# 90'''

# #WAP To print name of student => Pass
# result={"shantanu":67,"shital":21,"pooja":97,"sneha":34}

# for i in result:
#     if result[i] >= 40:
#         print(i)
# #shantanu
# #pooja      

# for name,per in result.items():
#     if per >= 40:
#         print(name)
# '''shantanu
# pooja'''


#Q.4 WAP to print list of students name who failed
result={"Shantanu":67,"Shital":21,"Pooja":97,"Sneha":34}

l=[]

for i in result:
    if result[i]<40:
        l.append(i)

print(l)

#['Shital', 'Sneha']