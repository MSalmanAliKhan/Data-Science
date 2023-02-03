# Input a number and give a dictionary with the cubes upto that number as output
cube=int(input("Enter the number upto which the dictionary is to be created "))
def cube_dict(n):
    diction={}
    for i in range(1,n+1):
        diction[i]=i**3
    return diction

print(cube_dict(cube))
