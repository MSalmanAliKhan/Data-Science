# A function that takes a list and counts the number of lists within that list
# num=int(input("Enter  the number of elements in the list "))
# lst=[]
# for i in range(num):
#     e=input("Enter list item ")
#     lst.append(e)
lst2=[2, "salman", [4,"salman",5],[2]]
def list_element_type(l):
    new_list=[]
    int=0
    str=0
    lst=0
    for j in range(len(l)):
        print (f"The list item {l[j]} is of {type(l[j])}")
        if type(l[j]) == type(2):
        # if type(l[j]) == int: can also be used
         int+=1
        elif type(l[j]) == type("s"):
         str+=1
        else:
         lst+=1
    print (f"There are {int} integers in {l}" )
    print (f"There are {str} strings in {l}" )
    print (f"There are {lst} lists in {l}" )
list_element_type(lst2)


