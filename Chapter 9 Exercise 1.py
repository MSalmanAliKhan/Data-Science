# Take a user input list and reverse all its strings.
l= input("Enter elements of the list ").split(",")
def rev_list(s):
    m=[i[::-1] for i in s]
    return m
print(rev_list(l))
