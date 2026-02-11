#type: ignore
#STRING: It is collection of character

#      0123456789
#name="Pruthviraj"

#Indexing: Single Element Fetch karne ke liye
# Slicing: Multiple Element fetch karne ke liye

# name="Pruthviraj"
# print(name[1])
# print(name[0:-3:1])
# print(name[-1:-4:-1])

#default value:

#Start Index
# name="rajesh"
# print(name[0:3:1])#raj
# print(name[:3:])#raj
# print(name[:3:1])#raj
# print(name[-1:-4:-1])#hse
# print(name[:-4:-1])#hse


# #End Index

# print(name[2:6:1])#jesh
# print(name[2::1])#jesh
# print(name[2::-1])#jar
# print(name[2:-7:-1])#jar


# #Step Value: By default step value is One

# print(name[0:-3:1])#raj
# print(name[0:-3])#raj
# print(name[0:-1:2])
# print(name[-1:-4:-1])


# name1="rameshwaram"
# print(name1[2:6])
# print(name1[:3])
# print(name1[-1:-4:])#ram
# print(name1[-3:])#ram
# print(name1[2::-1])#mar
# print(name1[-1:-4:-1])#mar
# print(name1[:-4:-1])#mar
# print(name1[2:7:2])#msw

#*****METHODS OF STRING******

#Function and Method both are block of code
#Method:Function which is under class
#To call method we access through object like object.function_name()

#Function:
#we can directly access through function name


#METHODS in Strings----------->

# name="rajesh"
# print(type(name))

# print(name.upper())
# print(name.lower())
# print(name)

# name1="Pooja"
# print(name1.upper())
# n=name1.upper()
# print(n)
# print(name1)

# name2="Bhakti"
# print(name2.lower())
# n1=name2.lower()
# print(n1)
# print(name2)


institute_name="the kiran academy"
# name=institute_name.upper()
# print(name)#THE KIRAN ACADEMY

# print(institute_name[4:9:1].upper())#KIRAN
# print(institute_name[10::].upper())#ACADEMY

# print(institute_name[-7::].upper())#ACADEMY
# print(institute_name[2::-1].lower())#eht

#TITLE
#each char first word is capital
print(institute_name.title())#each word is capitalize
print(institute_name.capitalize())#Only 1st word is capitalize

#Methods of STR
#var.method()


# Interview Question------->
# what is String?
# what is diff between capitalize and title?
#What is diff between function and method?
#how to call function and method?
