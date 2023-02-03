# Make a list which takes in a user generated list and gives a list with only the numbers of that list.
l=["a","b","c",[2,4,5],1,(2,3),{2,5},2.6,9,3,4]
def int_list(s):
    m=[str(i) for i in s if type(i) == int or type(i) == float]
    return m
print(int_list(l))
