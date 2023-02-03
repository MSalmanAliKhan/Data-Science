# Take a list and seperate the even and odd numbers in it in two seperate lists
num=int(input("Enter the number of elements in the list "))
lst=[]
for i in range(0,num):
    ele=int(input("Enter list item "))
    lst.append(ele)
def even_odd_list(l):
    even_list=[]
    odd_list=[]
    for i in l:
        if i%2==0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return odd_list, even_list
    # output = [odd_list, even_list] /n return output (Another option)
print(even_odd_list(lst))