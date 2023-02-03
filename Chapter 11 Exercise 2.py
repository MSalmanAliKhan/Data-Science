# A function that takes a list and makes the first letter capital but if reverse string is used
# it will reverse the string.
l=input("Enter the elements of the list ").split(",")
def upper_rev(*args,**kwargs):
    ls= [i[::-1].title() if kwargs.get('reverse_string') == True  else i.title() for i in args ]
    return ls
print(upper_rev(*l, reverse_string = False))
