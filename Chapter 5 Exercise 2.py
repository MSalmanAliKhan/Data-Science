# Take a user input list and reverse it
num=int(input("Enter the number of elements in the list "))
lst=[]
for i in range(0,num):
    ele=input("Enter list item ")
    lst.append(ele)
def reverse_list(l):
    r_list=[]
    for k in l:
# for k in range(len(l)): can also be used here
        r_list.append(l.pop())
    r_list.append(l.pop(0))
    return r_list
print(reverse_list(lst))

def reverse_list2(m):
    m.reverse()
    return m

def reverse_list3(m):
    return m[::-1]
