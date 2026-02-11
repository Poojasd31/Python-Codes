"""Conditional Statement"""
#IF ELSE STATEMENT
'''
Syntax:
if condition:
   #block of if
   #logic

else:
  #block of else
'''
#Example 1

# per = eval(input('Enter Your Percentage:'))

# if per > 90:
#     print("You are eligible for  government college")

# else:
#     print("You are eligible for Private college")

# print("Thank You!!!")

'''Output:=>
Enter Your Percentage:97
You are eligible for  government college
Thank You!!!

Enter Your Percentage:85
You are eligible for Private college
Thank You!!!
'''

#Example 2
#WAP TO CHECK NUMBER IS EVEN OR ODD
# num = eval(input("Enter a Number=>"))

# if num%2 == 0:
#     print("Number is Even")

# else:
#     print("Number is Odd")

'''
Enter a Number=>10
Number is Even

Enter a Number=>5
Number is Odd
'''

#Example 3
#WAP TO CHECK NUMBER IS POSITIVE AND NEGATIVE

# num = eval(input("Enter a number=>"))

# if num > 0:
#     print("Number is Positive")

# else:
#     print("Number is Negative")

'''
Enter a number=>-1
Number is Negative

Enter a number=>5
Number is Positive
'''

#Example 4
#WAP TO PRINT LIST OF EVEN NUMBERS AND LIST ODD NUMBERS FROM GIVEN LIST

# l=[11,22,33,44,55,66]
# l_even=[]
# l_odd=[]
# for num in l:
#     if num%2==0:
#         l_even.append(num)
#     else:
#         l_odd.append(num)

# print("Even List",l_even)
# print("Odd List",l_odd)

#Even List [22, 44, 66]
#Odd List [11, 33, 55]

#Example 5
#WAP TO PRINT LIST OF square EVEN NUMBERS AND LIST of cube ODD NUMBERS FROM GIVEN LIST
# l=[11,22,33,44,55,66]
# l_even=[]
# l_odd=[]

# for num in l:
#     if num%2==0:
#         l_even.append(num**2)
#     else:
#         l_odd.append(num**3)

# print(l_even)
# print(l_odd)

'''
[484, 1936, 4356]
[1331, 35937, 166375]
'''

#Example 6
#WAP WAP TO PRINT set of cube even nubers
#and set of square odd numbers from given list

# l=[1,2,3,4,5,6]
# cube_even=set()
# square_odd=set()

# for num in l:
#     if num%2==0:
#         cube_even.add(num**3)
#     else:
#         square_odd.add(num**2)

# print(cube_even)
# print(square_odd)
'''
{8, 64, 216}
{1, 9, 25}
'''
#EXAMPLE 7
#WAP TO PRINT list of cube even nubers
#and set of square odd numbers from given list
# l=[1,2,3,4,5,6]
# l_even=[]
# s_odd=set()

# for num in l:
#     if num%2==0:
#         l_even.append(num**3)
#     else:
#         s_odd.add(num**2)
# print(l_even)
# print(s_odd)
#[8, 64, 216]
#{1, 9, 25}

#Example 8
#WAP TO PRINT LIST OF NAME OF PASSED STUDENT AND 
#LIST of name fail student
# result={
#     'kunal':89,'ajay':32,"arun":67,
#     'vijay':36,'pavan':79,'harish':90
#     }
# pass_student=[]
# fail_student=[]

# for i in result:
#     if result[i]>40:
#         pass_student.append(i)
    
#     else:
#         fail_student.append(i)
# print(pass_student)
# print(fail_student)

#['kunal', 'arun', 'pavan', 'harish']
#['ajay', 'vijay']

result={
    'kunal':89,'ajay':32,"arun":67,
    'vijay':36,'pavan':79,'harish':90
    }

dict_pass = {}
dict_fail = {}

for name, per in result.items():
    if  per >40:
        dict_pass[name]=per
    
    else:
        dict_fail[name]=per

print(dict_pass)
print(dict_fail)

#{'kunal': 89, 'arun': 67, 'pavan': 79, 'harish': 90}
#{'ajay': 32, 'vijay': 36}