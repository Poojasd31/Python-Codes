#DICTIONARY
#CRUD
#Methods of Dict

'''Dict is a comma separated key value pai pair within curly braces'''
#key==>Unique and immutable
#value=>duplicate and both
# oppo_a14={"brand":"oppo","model":"a14","ram":"8gb","color":"black"}
# oppo={
#     'a14':"8GB","a15":"12GB"
# }

# oppo={
#     'a14':{'ram':'8gb','color':'black'},
#     'a15':{'ram':'12gb','color':'white'}
# }

#mobile dict => 2brand=> 2 model

# mobile={
#     "Oppo":{'Model1':"Oppo A55","Model2":"Oppo A76"},
#     "Vivo":{"Model1":"Vivo Y83","Model2":"Vivo Y81"}
# }
# print(mobile)

#Solution

# oppo={'a14':{'ram':"8gb",'color':"black"},
#       'a15':{'ram':"12gb",'color':"black"},
#       'a16':{'ram':"16gb",'color':"black"}
#       }

# mobile={
#     'oppo':{'a14':{'ram':"8gb",'color':"black"},
#       'a15':{'ram':"12gb",'color':"black"}
#       },
#     'vivo':{
#         'V7':{'ram':"8gb",'color':"black"},
#       'V9':{'ram':"12gb",'color':"black"},
#     }, 
# }
# print(mobile)

#Fav movie details(hero,heroin, release year,)

# Titanic={"hero":"Leonardo DiCaprio","Heroine":"Kate Winslet",
#        "Release Year":1997 , "Timing":"3H 14M"}
# print(Titanic)
# #{'hero': 'Leonardo DiCaprio', 'Heroine': 'Kate Winslet', 
# # 'Release Year': 1997, 'Timing': '3H 14M'}

# leonardo = {
#     "Titanic":{"Heroine":"Kate Winslet",
#        "Release Year":1997 , "Timing":"3H 14M"},
#     "The Revenant":{"Heroine":"Grace Dove", 
#         "Release Year":2015 , "Timing":"2H 36M"}
# }
# print(leonardo)

# # movie name dictionary and =>under 2 hero => 2 movie
# movie={
#     "Akshay Kumar":{
#     "Welcome":{
#         "Heroine":'Katrina',"Genre":"Comedy","Year of Release":2007
#     },
#     "Phir Hera Pheri 2":{
#        "Heroine":"Rimi Sen","Genre":"Comedy", "year of Relese":2005
#     }
#     },
#     "Salman Khan":{
#            "Tiger":{
#         "Heroine":'Katrina',"Genre":"Action","Year of Release":2010
#     },
#     "Tiger Jinda Hai":{
#        "Heroine":"Katrina","Genre":"Action", "year of Relese":2019
#     }
#        }
#     }
# print(movie)


'''
CRUD Operation
CRETAE
READ
UPDATE
DELETE
'''
#How to access data from dict
#Syntax:
#var[key]     -----> Return Value

#How to access data from dict
# oppo_14={"ram":"8gb","color":"black"}
# print(oppo_14['color']) #black

# #One brand multiple models
# oppo={'a14':{'ram':"8gb",'color':'black'},
#       'a15':{'ram':"12gb",'color':'white'},
#       'a16':{'ram':"16gb",'color':'pink'}
#       }

# print(oppo['a15']["ram"]) #12gb

# #a16color
# print(oppo["a16"]["color"]) #pink

#print(mobile['vivo'])

# print(mobile['vivo']['v20'])
# print(mobile['vivo']["v21"]['color'])

# mobile={
#     'oppo':{'a14':{'ram':"8gb",'color':"black"},
#       'a15':{'ram':"12gb",'color':"black"}
#       },
#     'vivo':{
#         'V7':{'ram':"8gb",'color':"black"},
#       'V9':{'ram':"12gb",'color':"black"},
#     }, 
# }

# print(mobile['oppo'])
# #{'a14': {'ram': '8gb', 'color': 'black'}, 
# # 'a15': {'ram': '12gb', 'color': 'black'}}

# print(mobile['vivo'])
# #{'V7': {'ram': '8gb', 'color': 'black'}, 
# # 'V9': {'ram': '12gb', 'color': 'black'}}

# print(mobile['vivo']['V9'])
# #{'ram': '12gb', 'color': 'black'}

# print(mobile['oppo']['a15']['color'])
# #black

"""How to add data
Syntax:
var[key]=value
"""

# oppo_14={"ram":"8gb","color":"black"}
# oppo_14['storage']="16GB"
# print(oppo_14)
# #{'ram': '8gb', 'color': 'black', 'storage': '16GB'}

# oppo={'a14':{'ram':"8gb",'color':'black'},
#       'a15':{'ram':"12gb",'color':'white'},
#       'a16':{'ram':"16gb",'color':'pink'}
#       }

# oppo['a15']['storage']="16Gb"
# print(oppo)
# {'a14': {'ram': '8gb', 'color': 'black'}, 
# 'a15': {'ram': '12gb', 'color': 'white', 'storage': '16Gb'}, 
# 'a16': {'ram': '16gb', 'color': 'pink'}}

# oppo['a14']['storage']="12Gb"
# print(oppo)
# #{'a14': {'ram': '8gb', 'color': 'black', 'storage': '12Gb'}, 'a15': {'ram': '12gb', 'color': 'white', 'storage': '16Gb'}, 'a16': {'ram': '16gb', 'color': 'pink'}}  

# mobile={
#     'oppo':{'a14':{'ram':"8gb",'color':"black"},
#       'a15':{'ram':"12gb",'color':"black"}
#       },
#     'vivo':{
#         'V7':{'ram':"8gb",'color':"black"},
#       'V9':{'ram':"12gb",'color':"black"},
#     }, 
# }

# mobile['oppo']['a14']['storage']='8gb'
# print(mobile)
#{'oppo':
#  {'a14': {'ram': '8gb', 'color': 'black', 'storage': '8gb'},
# 'a15': {'ram': '12gb', 'color': 'black'}}, 
# 'vivo': {'V7': {'ram': '8gb', 'color': 'black'}, 
#          'V9': {'ram': '12gb', 'color': 'black'}}}

JBK={
    "Python":{
        "Batch-1195":{
            "Roll No.1":{"Name":"Trupti","City":"Pune","Age":20},
            "Roll No.2":{"Name":"Sayali","City":"Ahilyanagar","Age":21}
        },
        "Batch-1205":{
            "Roll No.1":{"Name":"Anagha","City":"Nashik","Age":19},
            "Roll No.2":{"Name":"Niyati","City":"Nagpur","Age":22}
        }
     },
    "Java":{
        "Batch-1176":{
           "Roll No.1":{"Name":"Ayush","City":"Solapur","Age":23},
           "Roll No.2":{"Name":"Aman","City":"Satara","Age":19} 
        },
        "Batch-1188":{
            "Roll No.1":{"Name":"Raj","City":"Dharashiv","Age":19},
            "Roll No.2":{"Name":"Rahul","City":"Nashik","Age":20}
        }
     }
}

print(JBK)

#{'Python': {'Batch-1195': {'Roll No.1': {'Name': 'Trupti', 'City': 'Pune', 'Age': 20}, 
# 'Roll No.2': {'Name': 'Sayali', 'City': 'Ahilyanagar', 'Age': 21}}, 
# 'Batch-1205': {'Roll No.1': {'Name': 'Anagha', 'City': 'Nashik', 'Age': 19}, 
# 'Roll No.2': {'Name': 'Niyati', 'City': 'Nagpur', 'Age': 22}}}, 
# 'Java': {'Batch-1176': {'Roll No.1': {'Name': 'Ayush', 'City': 'Solapur', 'Age': 23}, 
# 'Roll No.2': {'Name': 'Aman', 'City': 'Satara', 'Age': 19}}, 
# 'Batch-1188': {'Roll No.1': {'Name': 'Raj', 'City': 'Dharashiv', 'Age': 19},
#  'Roll No.2': {'Name': 'Rahul', 'City': 'Nashik', 'Age': 20}}}}

JBK['Python']["Batch-1205"]["Roll No.1"]["Email"]="anagha123@gmail.com"
print(JBK)
#{'Python': {'Batch-1195': {'Roll No.1': {'Name': 'Trupti', 'City': 'Pune', 'Age': 20}, 
# 'Roll No.2': {'Name': 'Sayali', 'City': 'Ahilyanagar', 'Age': 21}}, 
# 'Batch-1205': {'Roll No.1': {'Name': 'Anagha', 'City': 'Nashik', 'Age': 19, 'Email': 'anagha123@gmail.com'}, 
# 'Roll No.2': {'Name': 'Niyati', 'City': 'Nagpur', 'Age': 22}}}, 
# 'Java': {'Batch-1176': {'Roll No.1': {'Name': 'Ayush', 'City': 'Solapur', 'Age': 23}, 
# 'Roll No.2': {'Name': 'Aman', 'City': 'Satara', 'Age': 19}}, 
# 'Batch-1188': {'Roll No.1': {'Name': 'Raj', 'City': 'Dharashiv', 'Age': 19}, 
# 'Roll No.2': {'Name': 'Rahul', 'City': 'Nashik', 'Age': 20}}}}

JBK['Java']['Batch-1176']["Roll No.2"]["City"]="Junnar"
print(JBK)
#{'Python': {'Batch-1195': {'Roll No.1': {'Name': 'Trupti', 'City': 'Pune', 'Age': 20}, 
# 'Roll No.2': {'Name': 'Sayali', 'City': 'Ahilyanagar', 'Age': 21}}, 
# 'Batch-1205': {'Roll No.1': {'Name': 'Anagha', 'City': 'Nashik', 'Age': 19}, 
# 'Roll No.2': {'Name': 'Niyati', 'City': 'Nagpur', 'Age': 22}}}, 
# 'Java': {'Batch-1176': {'Roll No.1': {'Name': 'Ayush', 'City': 'Solapur', 'Age': 23}, 
# 'Roll No.2': {'Name': 'Aman', 'City': 'Junnar', 'Age': 19}}, 
# 'Batch-1188': {'Roll No.1': {'Name': 'Raj', 'City': 'Dharashiv', 'Age': 19}, 
# 'Roll No.2': {'Name': 'Rahul', 'City': 'Nashik', 'Age': 20}}}}