# Count how many times a letter is repeated in a user entered name
name=input("Enter your full name ")
i=0
temp_variable=""
while i<len(name):
    if name[i] not in temp_variable:
     temp_variable+= name[i]
     print (f"{name[i]} is repeated {name.count(name[i])} times in {name} ")
    i=i+1

