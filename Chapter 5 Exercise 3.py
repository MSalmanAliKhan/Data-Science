# Take a user input list and reverse the letters of each of its item
num=int(input("Enter the number of elements in the list "))
lst=[]
for i in range(0,num):
    ele=input("Enter list item as a group of words ")
    lst.append(ele)
def rev_list(l):
    new_list=[]
    for i in l:
       new_list.append(i[::-1])
    return new_list
print(rev_list(lst))
