''' 
  Lets Understaned Higher Order Function (HOF)
  
  HOF if Function which will accept argument as function
  and return function as well.

  NOTE : Use Debugger to Understand the flow of code.
'''

''' Example '''
# 1
print('\nHigher Order Function\n')
def Login(func,username,password):
  isValid = func(username, password)
  if isValid:
    return f'Welcome {username}'
  else:
    return 'Invalid username or password... ?'
  
def validate_user_data(temp_uname, temp_pass):
  if temp_uname.strip()=='Mike' and temp_pass.strip()=='mikeee128':
    return True
    
def get_user_details():
  uname = str(input('Enter your username:'))
  passwrd = str(input('Enter your password:'))

  return uname,passwrd

if __name__=='__main__':
  usrname, paswd = get_user_details()
  print(f'1.{Login(validate_user_data, usrname, paswd)}')


''' 
  In above example i have created 3 function but if you Notice
  In "Login" Function i have passed the "validate_user_data" as 
  an arrgument and used that function future in my code. 
'''
print('#'*58)
####################################################################################################################################################################################################################################################################################################################

''' Currying '''

'''
  We can use higher-order functions to convert a function that takes 
  multiple arguments into a chain of functions that each take a single
  argument. More specifically, given a function f(x, y), we can define
  a function g such that g(x)(y) is equivalent to f(x, y). Here, g is a
  higher-order function that takes in a single argument x and returns 
  another function that takes in a single argument y. This transformation 
  is called currying.
'''
''' Example '''

print('\n\nCurrying\n')
# 1. 
def get_1st_number(num_1):
  def get_2nd_number(num_2):
    return num_1+num_2

  return get_2nd_number

if __name__=='__main__':
  print(f'1. Addition of two Number: {get_1st_number(10)(20)}')

''' The above function is pure function because is completely depend on input.'''

# 2.
def pas_function(user_func):
  def get_x(x):
    def get_y(y):
      return user_func(x,y)
    return get_y
  return get_x

def mul_function(a,b):
  return a+b

pas_func = pas_function(mul_function)
print(f'2. Currying With user define or pre define function:{pas_func(2)(4)}\n')

''' 
  In above example you can apply any function which applicable for two arrguments such as "max","min", "pow". etc.
  You can also passs user define function ..in our case i have passed "mul_function", you guys can yours
  Function but make sure that function will work on 2 prameter.
'''
print('#'*58)
####################################################################################################################################################################################################################################################################################################################

''' Higher Order Function With Currying '''
print('\nHigher order fucntion with Currying\n')
#1.

def Login(func,welcom_func):
    def get_username(uname):
        def get_password(pas):
            isValid = func(get_user_details,uname,pas)
            if isValid:
                return welcom_func(uname)
            else:
                return Invalid_user()
        return get_password
    return get_username

def check_valid_User(func_user_input,usernm,userpas):
    tempUname,tempPass = func_user_input()
    return ((tempUname.strip()==usernm) and (tempPass.strip()==userpas.strip()))

def welcome_user(uname):
    return f'Welcome {uname}'

def Invalid_user():
    return 'invalid username or password'

def get_user_details():
    tempName = str(input('Username:'))
    tempPass = str(input('Password:'))
    return str(tempName).strip(), str(tempPass).strip()

login = Login(check_valid_User,welcome_user)
print(login('Mike')('Mikeee'))
print('#'*58)
