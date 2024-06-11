# Datatype

number = 78 #Int
num = 45.09 #float
greeting = "How are you doing today?" #str
Is_Programming_Intresting = True #bool
devices = ["Laptop","Computer","Tablet","Phone"] #list
browsers = ( "Opera","firefox","chrome","safari") #Tuple
countries = {"kenya", "Uganda","Tanzania"} # set
employee = {
    "first_name": "John",
    "age" : 29,
    "nationality" : "Kenyan",
    "emailaddress" : "John@gmail.com",
} #Dictionary
print(Is_Programming_Intresting)
print(num)
print(countries)
print(employee["first_name"])


# Determining a datatype
print(type(countries))
print(type(employee))


# Typecasting is the process of converting one datatype to another
print(int(num))
print(float(number))