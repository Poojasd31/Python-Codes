#www.thekiranacademy.com/test

#Todays Agenda:
'''
Data Type:
Dict
How to create Dict
'''
#Data Type--> It is predefined class. 
#It represent data
#It tells us which operation we performed on data

'''
Data Type:
str -> '' or "" -> Immutable

list -> [] or list() -> Mutable -> Order -> HCE - Duplicates allowed

tuple -> () or tuple() -> immutable -> Order ->HCE Duplicates allowed

set ()-{v1,v2} ->Mutable -> Unorder -> HCIE-Duplicates not allowed

'''

# l=[11,4,77,3,99]
# l.sort(reverse=True)
# print(l)

#DICTIONARY
'''
Important Data Type-> List and Dict
To store number from 1 to 10 we can use list/tuple/set

var_name={k1:v1,k2:v2,........}

It is comma separated key-value pair within curly braces.


'''
#Dictionary

# details={'name':'raj','age':24,'per':89,'ac':1234567,'mob':9876543212}
# print(type(details))  #<class 'dict'>

# square={1:1,2:4,3:9,4:16,5:25}

'''
KEY==>
1. Key should be unique
2. It should be Immutable
3. d={2:4,"name":"Rajesh",1.1:"xyz",(1,2,3):(1,4,9)}
'''
# details={"name":"rajesh","age":24}
# print(details) #{'name': 'rajesh', 'age': 24}

# details={"name":"rajesh","age":24,"name":"vaibhav"}
# print(details) #{'name': 'vaibhav', 'age': 24}===> The name is updated because duplicates are not allowed it only have unique values

# # d={2:4,"name":"Rajesh",1.1:"xyz",(1,2,3):(1,4,9),[1,2,4]:[1,4,81]}
# #O/P==> TypeError: unhashable type: 'list'

# d={2:4,"name":"Rajesh",1.1:"xyz",(1,2,3):(1,4,9)}
# print(d) #{2: 4, 'name': 'Rajesh', 1.1: 'xyz', (1, 2, 3): (1, 4, 9)}

'''
Value:
1. Value may be DUPLICATE, MUTABLE OR IMMUTABLE
'''
#For Ex->

details={"name":'raj','age':29,'per':29}
#Value may be same

#Key can Mutable or Immutable
details={'name':'Pooja','age':29,'per':29,'marks':{'math':89,'scie':45}}
print(details)
#{'name': 'Pooja', 'age': 29, 'per': 29, 'marks': {'math': 89, 'scie': 45}}

'''Dict is a comma separated value within key and value pair'''
'''Key=>Should be Unique and Immutable'''
'''Value=> Duplicate, Mutable, Immutable'''

#1. Create dict=>Own details
my_dict = {'name':"Pooja",'city':"Ahilyanagar",'Education':"Engineering",'mobile':000000000,'country':"India"}
print(my_dict)
#{'name': 'Pooja', 'city': 'Ahilyanagar', 'Education': 'Engineering', 'mobile': 0, 'country': 'India'}

#2. Create dict square of number from 10-15
square={10:100,11:121,12:144,13:169,14:196,15:225}
print(square)
#{10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
square={11:11**2,12:12**2}
print(square)
#{11: 121, 12: 144}

#3. Dict mobile details
mobile={"Brand":"Samsung","Model":"M13 4G","Storage":"64GB","RAM":"4GB","Color":"Blue","Camera":"50MP"}
print(mobile)
#{'Brand': 'Samsung', 'Model': 'M13 4G', 'Storage': '64GB', 'RAM': '4GB', 'Color': 'Blue', 'Camera': '50MP'}
print(type(mobile)) #<class 'dict'>

#4.Star Details
star ={"star_name":"M S Dhoni","Birth Date":"07/07/1981","Role":"Wicket-Keeper batsman","Nick Name":"Mahi","Wife_Name":"Sakshi","Daughter":"Ziva"}
print(star)
#{'star_name': 'M S Dhoni', 'Birth Date': '07/07/1981', 'Role': 'Wicket-Keeper batsman', 'Nick Name': 'Mahi', 'Wife_Name': 'Sakshi', 'Daughter': 'Ziva'}

#Dict=> 3 student details

students={1:{"Name":"Pooja","City":"Pune"},
          2:{"Name":"Shraddha","City":"Nagar"},
          3:{"Name":"Bhakti","City":"Mumbai"}}
print(students) 
#{1: {'Name': 'Pooja', 'City': 'Pune'}, 
# 2: {'Name': 'Shraddha', 'City': 'Nagar'},
# 3: {'Name': 'Bhakti', 'City': 'Mumbai'}}

#One plus two model details
Samsung={
    'M14':{'Ram':"8gb",'storage':'64GB','Camera':"50MP",'Price':8000},
    'M15':{"Ram":"12gb",'storage':"128gb","Camera":"50MP","Price":10000}
}

print(Samsung)
#{'M14': {'Ram': '8gb', 'storage': '64GB', 'Camera': '50MP', 'Price': 8000},
# 'M15': {'Ram': '12gb', 'storage': '128gb', 'Camera': '50MP', 'Price': 10000}}

#Car Brand => 3 brand details email karne hai
#IQ
'''WHAT IS DICT
HOW TO CREATE DICT IN PYTHON
CAR BRAND=> 3 CAR DETAILS 
'''

car_brands={
    "Toyota":{"Model":"Camry","Year":2022,"Color":"Blue","Price":25000},
    "Honda":{"Model":"Civic","Year":2021,"Color":"Red","Price":22000},
    "Ford":{"Model":"Mustang","Year":2020,"Color":"Black","Price":30000}
}
print(car_brands)
#Output
#{'Toyota': {'Model': 'Camry', 'Year': 2022, 'Color': 'Blue', 'Price': 25000}, 
# 'Honda': {'Model': 'Civic', 'Year': 2021, 'Color': 'Red', 'Price': 22000}, 
# 'Ford': {'Model': 'Mustang', 'Year': 2020, 'Color': 'Black', 'Price': 30000}}