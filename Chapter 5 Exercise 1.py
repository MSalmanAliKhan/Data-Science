# Take a user input list and output a list with all its elements squared
lst_range= int(input("Enter the number of elements in the list "))
lst=[]
for i in range(0,lst_range):
    ele=input("Enter the element ")
    lst.append(ele)
def square_of_list(l):
    sq_list=[]
    for k in l:
        sq_list.append(int(k)**2)
    return sq_list
print(square_of_list(lst))
