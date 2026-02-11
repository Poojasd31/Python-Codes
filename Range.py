#TOday's Agenda
#for loop
#data type: RANGE

'''FOR LOOP / for loop'''
# for loop:
'''
1. To do Iteration
l=[11,22,33]
o/p->
11
22
33
'''
#Syntax:  
'''
for var in iterable:
   #body/block

for=> Keywords
in => Keywords
iterable=> Perform for loop--> Strings, List, Set,Tuple

Note:: For loop not applied to int, float, complex and bool

':' header part ends and body part started
and that space is called indentation(4 Space) or minimum 1 space

Body/block: Statement , Code, Logic

'''
#When iteration word comes use for loop

l=[11,22,33,44,55]
#l is Iterable
print(len(l)) #5 #To know length

for num in l:
    print(num)
'''
Output:
11
22
33
44
55 #and this process is called iteration
'''

l=[1,2,3]
for num in l:
    print(num)
print('Hello')
'''
1
2
3
Hello
'''
#Indentation means White Space

print('Hello')
l=[1,2,3]
for num in l:
    print(num)
    print("JBK")
print("End")

'''
Hello
1
JBK
2
JBK
3
JBK
End
'''

name="Pooja Dhakane"
for char in name:
    print(char)

'''
Output:
P
o
o
j
a

D
h
a
k
a
n
e
'''

t=(11,22,33)
for num in t:
    print(num)
'''
11
22
33
'''
l=[1,2,3,4,5,6]
#WAP to print square of each number
for num in l:
    print(num," Square is=",num*num)

'''
1  Square is= 1
2  Square is= 4
3  Square is= 9
4  Square is= 16
5  Square is= 25
6  Square is= 36
'''

student=['jay','veeru','gabbar','thakur']

for name in student:
    print(name.upper())

'''
Output:

JAY
VEERU
GABBAR
THAKUR
'''

#DATA Type: RANGE
'''
object:

var=range(start_value,end_value,step_value)
range tooks 3 arguments
start_value=>start
end_value=>stop before end value
step=> difference

r=range(1,11,1)

'''
r=range(1,11,1)
print(r) #range(1, 11)
print(list(r)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

r=range(1,21,1)
print(list(r)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(tuple(r)) #(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)

#Create a list of even numbers from 10 to 200
r = range(10,201,2)
print(list(r))
'''
[10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 
44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78,
 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 
 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138,
   140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 
   168, 170, 
172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200]
'''
r=range(1,10,1)
print(list(r)) ##[1, 2, 3, 4, 5, 6, 7, 8, 9]
r=range(1,10)
print(list(r)) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
r=range(10)
print(list(r)) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#If single value is given then it is stop

l1=list(range(1,11,1))
print(l1)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2=list(range(1,11))
print(l2)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l3=list(range(11))
print(l3)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


print('ITERATION')
r=range(1,11,1)
for i in r:
    print(i)
'''
O/P:
1
2
3
4
5
6
7
8
9
10
'''

for i in range(1,11,1):
    print(i)
'''
1
2
3
4
5
6
7
8
9
10
'''
#WAP TO PRINT EVEN NUMBERS 12-20
print('EVEN Numbers')
for i in range(12,21,2):
    print(i)
'''
EVEN Numbers
12
14
16
18
20
'''
#10-1
print("Reverse")
for num in range(10,0,-1):
    print(num)
'''
Reverse
10
9
8
7
6
5
4
3
2
1
'''

# 1 to 5 square
print("Square of numbers from 1 to 5")
for num in range(1,6):
    print(num,"square is =",num*num)
'''
Square of numbers from 1 to 5
1 square is = 1
2 square is = 4
3 square is = 9
4 square is = 16
5 square is = 25
'''
#WAP TO PRINT CUBE ALL ODD NUMBERS FROM 22-30
# print("Cubes")
# for num in range(23,31,2):
#     print(num,"Cube is=", num*num)

'''
Cubes
23 Cube is= 529
25 Cube is= 625
27 Cube is= 729
29 Cube is= 841
'''

#WAP TO PRINT EVEN NUMBERS FROM 51-40
for i in range(50,39,-2):
    print(i)
'''
50
48
46
44
42
40
'''
#INTERVIEW QUESTIONS
#Range or for loop test certificate