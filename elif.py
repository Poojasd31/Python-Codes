#Conditional Statement
"""
If Elif Else Statement
"""

#two students=> akshay,harshad=>Age

# s1=int(input("Enter age for s1=>"))
# s2=int(input("Enter age for s2=>"))

# if s1>s2:
#     print("s1 is greater than s2")

# else:
#     print("s2 is greater than s1")

'''
Enter age for s1=>19
Enter age for s2=>17
s1 is greater than s2

Enter age for s1=>17
Enter age for s2=>19
s2 is greater than s1
'''

#For Multiple statement we have to used ELIF statement
# We can use Multiple elif statement
#If IF block executed then other conditions not going to check 
#IF condition is false then it will go to the ELIF block and it will execute
#Otherwise it will execute Else block. If all the above conditions is false

#Example 2

# s1=int(input("Enter age for s1=>"))
# s2=int(input("Enter age for s2=>"))
# s3=int(input("Enter age for s3=>"))

# if s1>s2 and s1>s3:
#     print("s1 is greater than s2 and s2")

# elif s2>s1 and s2>s3:
#     print("s2 is greater than s1 and s3")

# else:
#     print("s3 is greater than s1 and s2")

'''
Enter age for s1=>18
Enter age for s2=>19
Enter age for s3=>17
s2 is greater than s1 and s3

Enter age for s1=>12
Enter age for s2=>13
Enter age for s3=>16
s3 is greater than s1 and s2

Enter age for s1=>21
Enter age for s2=>18
Enter age for s3=>15
s1 is greater than s2 and s2
'''
#Example 3
#WAP to check number is Positive
#negative and 0

# num = eval(input("Enter a number=>"))

# if num>0:
#     print("Number is Positive!")

# elif num<0:
#     print("Number is Negative!")

# else:
#     print("Number is Zero!")

'''
Enter a number=>0
Number is Zero!

Enter a number=>5
Number is Positive!

Enter a number=>-2
Number is Negative!
'''
#Example 4
#Calculator=>2 Number

# num1=eval(input("Enter a Number1=> "))
# symbol=str(input("Enter a symbol which you want to calculate=>"))
# num2=eval(input("Enter a Number2=> "))

# if symbol=='+':
#     print("Addition=>",num1+num2)

# elif symbol=='-':
#     print("Subtraction=>",num1-num2)

# elif symbol=='/':
#     print("Division=>",num1/num2)

# elif symbol=="*":
#     print("Multiplication=>",num1*num2)

# else:
#    print("Invalid Operator!")

'''
Enter a Number1=> 24
Enter a Number2=> 2
Enter a symbol which you want to calculate=>/
Division=> 12.0

Enter a Number1=> 24
Enter a Number2=> 24
Enter a symbol which you want to calculate=>*
Multiplication 576

Enter a Number1=> 124
Enter a Number2=> 2
Enter a symbol which you want to calculate=>+
Addition=> 126

Enter a Number1=> 120
Enter a Number2=> 10
Enter a symbol which you want to calculate=>-
Subtraction=> 110
'''

#Example 5
#Subjects => Marks => Grade
# >90 = A+ grade
#80-90 = A grade
#70-80 B+
#60-70 B
#60 => C

# marks=eval(input("Enter your marks=>"))

# if marks>90:
#     print("Grade=>A+")
# elif marks>80:
#     print("Grade=>A")
# elif marks>70:
#     print("Grade=>B+")
# elif marks>60:
#     print("Grade=>B")
# else:
#     print("Grade=>C")

'''
Enter your marks=>90
Grade=>A

Enter your marks=>61
Grade=>B
'''
#Example 6
#dict=>name=key and age=value
#list print3 category 10-20 age, 20-40 age and 40 above

dict={
    'Bhakti':24, 'Pragati':17,'Raavi':34,
    'Adesh':23,'Rahul':45,'Arjun':75,
    'Ahana':74,'Kartik':65,'Maya':34,
    'Arti':32
}
l1=[]
l2=[]
l3=[]

for name,age in dict.items():
    if age>10 and age<20:
        l1.append(name)
    
    elif age>20 and age<40:
        l2.append(name)
    
    else:
        l3.append(name)
    


print(l1)
print(l2)
print(l3)

'''
['Pragati']
['Bhakti', 'Raavi', 'Adesh', 'Maya', 'Arti']
['Rahul', 'Arjun', 'Ahana', 'Kartik']
'''