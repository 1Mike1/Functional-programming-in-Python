"""
  lambda Function also know as Anonymous Functions.
  We can use lambda as inline Function.
  
  lambda is keyword of python which is use to define a
  lambda Function for single line operation in programing.

  We can't use lambda Function for multiline, So while 
  creating any lambda Function please keep this in mind and
  write your code accordingly.

  # How to Define lambda Function:
    syntax:

    lambda_Function = lambda return_value: parameter + 10
    lambda_Function(User Define)

    e.g:-
      l_fun = lambda x:x+10
      print(l_fun(10))

    Note:
      l_fun = Generate by lambda Function which need some parameter to 
              run the above code.
      x = as you can see that i have passed '10' as parameter to my lambda
          Function (l_fun(10)). '10' is the value of x.

  # How to convert Normal Function into lambda Function:

    # Normal Function
      def add(x):
        return x+10
    
    # lambda Function
      lambda x:x+10

    Note:
      To convert the Normal Function into lambda follow this steps.
        1. Replace 'def function_name' with 'lambda'.
        2. Declare variable after lambda which will hold you parameter,
           in our case we have 'x'.
        3. Now You are good to go with programing logic after ':'.

        e.g:-
            1. Replaceing 'def add'
               def add -> lambda 

            2. Now We need a parameter i.e 'x' in our case
               def add(x): -> lambda x:
            
            3. Logic Part for Addition
               x+10

            Once you have done with above part you will get your
            lambda Function, which is something like this.
              
              Function: lambda x:x+10

    # For More understanding, please check out my below Examples.
"""

#Example of lambda Function

#Addiotion Using lambda Function
add = lambda a:a+10
print('\nAddition is:',add(20))

#Lambda Function To Concatinate Two String
First_Last_name = lambda a,b:str(a)+' '+str(b)
print('\nFull name:',First_Last_name('Mithlesh','kumar'))

#Printing Table using lambda Function
table = lambda n:[n*i for i in range(1,11)]
print('\nTable:',table(5))

#Sorting Name with last name using lambda Function
names=['Santy H','Abhi P','Kunal K','Mike G','Ritesh P','Shahin S']
names.sort(key=lambda name: name.split(' ')[-1].lower())
print('\nName Sorted by Last Name:\n',names)

#lambda Function within Function for (a+b)^2
def Multplication(b):
  return lambda x: x**2+b**2+2*x*b

lam_Fun=Multplication(4)
print('\n(a+b)^2 is:',lam_Fun(2))
#In above case we have passed the value of 'b' as '4' and then in lambda
#Function we have passed the value of 'a' as 2


#Uses of If and else in lambda Function
Find_Even_Odd = lambda x: print('\n{} is a Even Number'.format(x)) if x%2==0 else print('\n{} is a Odd Number'.format(x))
print(Find_Even_Odd(4))

#Squaring Number using lambda Function by excluding 5 using if statement
sqr=lambda x: [x*x for x in range(x) if x!=5]
print(sqr(10))


# Program to filter out only the even items from a list
num_list = [1, 5, 4, 6, 8, 11, 3, 12]
even_list = list(filter(lambda x: (x%2 == 0) , num_list))
print('Even Number List: ',even_list)