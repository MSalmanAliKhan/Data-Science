# Take a user input list and make its  element to the power of another element.
user=input("Enter the numbers of the list ").split(",")
power=int(input("Enter the exponent of the numbers "))
def num_exp(n,*args):
    l=[int(i)**n if i else print("You did not write any argument") for i in args]
    return l
print(num_exp(power,*user))

