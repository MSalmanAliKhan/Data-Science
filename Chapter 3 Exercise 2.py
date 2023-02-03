# Determine if a user can watch a movie depending on their age
name,age= input("Enter your name and age ").split(",")
if (name[0]=="a" or name[0]=="A") and int(age)>10:
    print("You can watch coco movie")
else:
    print("Sorry,you cannot watch coco movie")
