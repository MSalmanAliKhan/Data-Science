# Take two lists from the user and find the common elements in them
num1=int(input("Enter the number of elements in the first list "))
num2=int(input("Enter the number of elements in the second list "))
lst1=[]
lst2=[]
for i in range(num1):
    ele1=input("Enter the first list item ")
    lst1.append(ele1)
for j in range(num2):
    ele2=input("Enter the second list item ")
    lst2.append(ele2)   
def common_list(l1,l2):
    new_list=[]
    for k in l1:
        if k in l1 and k in l2:
         new_list.append(k)
    return new_list

print(common_list(lst1,lst2))


