#We need to create a variable 

myNum = 45
#You can also make myNum a user input

myNum = int(input("Enter a num: "))

#There is no command in Python like "even(45)"
#So we have to define it ourselves...
#Let's make a function called evenOrOdd

def evenOrOdd(x):
  #There will be one requirment, which is x. x will be an integer
  #We will use a modulo to find the remainder thing
  if x % 2 == 1:
    #If you divide a number by 2 and you get a remainder of 1, that means that the number is an odd number
    return f"The number {x} is an odd number"
  else:
    #In all other conditions (0), return even
    return f"The number {x} is an even number"
   
