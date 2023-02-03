# To raise error if user gives wrong input or divides a number by zero
# try:
#    x=int(input("Enter first number"))
#    y=int(input("Enter second number"))
# except ZeroDivisionError:
#    print ("Don't divide by zero")
# except ValueError:
#     print("Make sure that you enter a number and not a string")

x=int(input("Enter first number"))
y=int(input("Enter second number"))

def divide(a,b):
 try:
   return f"The division results in {a/b}" 
 except ZeroDivisionError:
   print("Don't divide by zero")
 except ValueError and TypeError:
   print("Make sure that you enter a number and not a string")
   

print(divide(4,'six'))
