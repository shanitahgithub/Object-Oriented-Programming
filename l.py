 #Creating a user class with properties name,age,location
 # Option1
class User:
    name='Shanitah'
    age=21
    location='Bukoto'
print(User)

# Option2
class User:
    def _init_ (User,name,age,location):
        User.name=name
        User.age=age
        User.location=location
name='Shanitah'          
age=21
location='Bukoto'
print(User)


# Creating a new instance of the User class  
# Option1
class User:
    name='Shanitah'
    age=21
    location='Bukoto'
User.data=User()           #Creating an instance of the User class and 
                           #storing it into the variable User.data
print(User.data.name)      
print(User.data.age)       # Accessing the User's name and age

# Option2
class User:                          # Parathensis are optional here
    def _init_ (User,name,age,location):
        name=User    # Creating an instance of the User class and storing it into a variable name
        age=User
name='Shanitah'          
age=21
print(name)
print(age)

# Function that prints a user's location
class User():
    def _init_(User,location):
     User.location=location
location='Bukoto'
print(location)
