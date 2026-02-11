#In poerator- To check membership
'''The in operator in Python checks if a specified 
value exists within a sequence, such as a list,
 tuple, or string.'''
# l=[11,22,33,44,55]
# print(33 in l)
# print(333 in l)

# True
# False

'''IS  Operator in Python'''
#he 'is' operator in Python is used to check if two variables 
# point to the same object. Unlike the '==' operator, 
# which checks if the values of two objects are equal,
#  the 'is' operator goes one 
# step further to ensure that they are, in fact, 
# the exact same object.
# l1=[11,22,33]
# l2=[11,22,33]

# print(id(l1))
# print(id(l2))
# print(l1 is l2)
# # 2106600839424
# # 2106600837504
# # False

# n1=100
# n2=100
# print(n1 is n2)
#True


#String Formatting
'''\n  -> New Line'''

# print("hello\nwelcome")
#hello
# welcome

'''\t - 4 space,1 tab'''
# print("hello\twelcome")
#hello   welcome


#sep attribute=>default value<=> " " Empty string
'''The sep parameter of the print() function is used to 
specify the separator between the strings. 
In the first example, a comma is used as the separator.'''

# a=100
# b=200
# c=300
# print(a,b,c) #100 200 300
# print(a,b,c,sep="@") # 100@200@300


#end attribute
#default value <=> '\n' set hoti hai
'''The end parameter in the print() function specifies
 what is printed at the end of the output. 
By default, it is set to a newline character ( \n )'''
# n1=100
# n2=100
# n3=100
# print(n1, end="\n")
# print(n2,end="\n")
# print(n3,end="\n")
#100
# 100
# 100

# print(n1, end="@")
# print(n2,end="@")
# print(n3,end="@")
#100@100@100@
'''SUM'''
# n1=100
# n2=200
# print('sum of',n1,'and',n2,'=',n1+n2)
# #sum of 100 and 200 = 300
'''Decimal Number=%d'''
# print('sum of %d and %d is %d'%(n1,n2,n1+n2))
#sum of 100 and 200 is 300

'''Multiplication'''
# n1=20
# n2=30
# print("multiplication of %d and %d is %d"%(n1,n2,n1*n2))
#multiplication of 20 and 30 is 600

'''Cube'''
# num=int(input("Enter num: "))
# print('Cube of %d is %d'%(num,num**3))
# Enter num: 2
# Cube of 2 is 8

'''Float <=> %f'''
# n1=float(input("enter num1=>"))
# n2=float(input("enter num2=>"))

# print("sum of %f and %f is %f"%(n1,n2,n1+n2))
# enter num1=>2.5
# enter num2=>2.5
# sum of 2.500000 and 2.500000 is 5.000000

# print("sum of %0.2f and %0.2f is %0.2f"%(n1,n2,n1+n2))
#sum of 2.50 and 2.50 is 5.00

# print("sum of %0.1f and %0.1f is %0.1f"%(n1,n2,n1+n2))
#enter num1=>1.1
# enter num2=>2.2
# sum of 1.1 and 2.2 is 3.3

# n1=float(input("enter num1=>"))
# n2=float(input("enter num2=>"))

# print("diff of %0.2f and %0.3f is %f0.4"%(n1,n2,n1-n2))
#enter num1=>2.34
# enter num2=>1.23
# diff of 2.34 and 1.230 is 1.1100000.4

'''%s==> For string'''
# name=input('Enter name=>')
# city=input('Enter City=>')
# print("my name is %s and I am from %s"%(name,city))

#Enter name=>Pooja
# Enter City=>Pune
# my name is Pooja and I am from Pune

'''format()'''
# Use placeholder and format method
# name=input('Enter name=>')
# city=input('Enter City=>')

# print("my name is {} and I am from {}".format(name,city))
#Enter name=>Pooja
# Enter City=>Ahmednagar
# my name is Pooja and I am from Ahmednagar

# print("my name is {0} and I am from {1}".format(city,name))
# Enter name=>Raavi
# Enter City=>Alandi  
# my name is Raavi and I am from Alandi
# my name is Alandi and I am from Raavi

# print("my name is {} and I am from {}".format(city,name))
#Enter name=>Pooja
# Enter City=>Pune
# my name is Pune and I am from Pooja

# print("my name is {1} and I am from {0}".format(city,name))
#Enter name=>Pooja
# Enter City=>Pune
# my name is Pooja and I am from Pune

# print("my name is {n} and I am from {c}".format(c=city,n=name))
#Enter name=>Pooja
# Enter City=>Nagar
# my name is Pooja and I am from Nagar

# print('my name is',name, 'i am from ',city)
# Enter name=>Pooja
# Enter City=>Pune
# my name is Pooja i am from  Pune

# num1=10
# num2=20
# print("sum of {} and {} is {}".format(num1,num2,num1+num2))
# #sum of 10 and 20 is 30

# print("sum of {1} and {2} is {0}".format(num1+num2,num1,num2))
# #sum of 10 and 20 is 30

# print("sum of {n1} and {n2} is {s}".format(s=num1+num2,n1=num1,n2=num2))
# #sum of 10 and 20 is 30

'''  f''   '''
# name='kunal'
# city="pune"
# print(f'my name {name} and i am from {city}')
# #my name kunal and i am from pune

'''Summary'''
# \n= NEW LINE
# \t= 1 TAB SPACE
# sep = " "
# end="\n"
# %d= int
# %f=float
# %s=STRING 
# format()
# f" "

# print('The','Kiran','Academy')
# #The Kiran Academy

# print('The','Kiran','Academy',sep="*")
# #The*Kiran*Academy

# print('Hello','Pooja')
# #Hello Pooja

# print("Hello","Pooja",end="!!!!")
# #Hello Pooja!!!!

# print("Enter your 3 subjects marks:==>")
# English=int(input("Enter marks for English Subjec:"))
# Marathi=int(input("Enter marks for Marathi Subjec:"))
# Hindi=int(input("Enter marks for Hindi Subjec:"))

# Sum = English+Marathi+Hindi

# print("Sum of three subjects i.e. %d , %d and %d is %d"%(English,Marathi,Hindi,Sum))

#Enter your 3 subjects marks:==>
# Enter marks for English Subjec:90
# Enter marks for Marathi Subjec:96
# Enter marks for Hindi Subjec:95
# Sum of three subjects i.e. 90 , 96 and 95 is 281

# radius=eval(input("Enter the Radius for Circle=>"))
# pi = eval(input("Enter PI value=>"))

# area = pi*(radius**2)

# print("Area of circle for radius %0.1f with PI value %0.2f is %0.3f"%(radius,pi,area))
# #Enter the Radius for Circle=>3
# # Enter PI value=>3.14
# # Area of circle for radius 3.0 with PI value 3.14 is 28.260
    
# print("Area of circle for radius {} with PI value {} is {}".format(radius, pi, area))
# #Enter the Radius for Circle=>3
# Enter PI value=>3.14
# Area of circle for radius 3.0 with PI value 3.14 is 28.260
# Area of circle for radius 3 with PI value 3.14 is 28.26

# name=input('Enter your Name=>')
# last_name=input("Enter your Last Name=>")
# school_name=input("Enter your School Name=>")
# print("My name is %s and last name is %s. My School name is %s"%(name,last_name,school_name))
# print("My name is {} and last name is {} and My School Name is {}".format(name,last_name,school_name))

# #Enter your Name=>Pooja
# # Enter your Last Name=>Dhakane
# # Enter your School Name=>Modern School
# # My name is Pooja and last name is Dhakane. My School name is Modern School
# # My name is Pooja and last name is Dhakane and My School Name is Modern School


# name = "Pooja"
# weight = 56
# height = 5.3
# print("my name is {}. My weight={} and Height={}".format(name,weight,height))
# #my name is Pooja. My weight=56 and Height=5.3

# print("my name is {n}. My weight={w} and Height={h}".format(n=name,w=weight,h=height))
# #my name is Pooja. My weight=56 and Height=5.3

# print("my name is {n}. My weight={w} and Height={h}".format(w=weight,h=height,n=name,))
# #my name is Pooja. My weight=56 and Height=5.3

x = 10
y = 5
print(f"{x} + {y} = {x + y}")
#10 + 5 = 15