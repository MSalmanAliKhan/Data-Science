# Create a user generated list and give output in  proper format
name=input("Enter your name: ")
age=input("Enter your age: ")
# n1=int(input("How many movies are your favourite: "))
# l1=[]
# for i in range(n1):
#    e1=input("Enter your favourite movie: ")
#    l1.append(e1)
# n2=int(input("How many songs are your favourite: "))
# l2=[]
# for k in range(n2):
#     e2=input("Enter your favourite song ")
#     l2.append(e2)
fav_mov=input("Enter your favourite movies seperated by comma ").split(",")
fav_song=input("Enter your favourite songs seperated by comma ").split(",")
D={}
D["name"]=name
D["age"]=age
# D["Favourite Movies"]=l1
# D["Favourite Songs"]=l2
D["Favourite Movies"]=fav_mov
D["Favourite Songs"]=fav_song
for m,n in D.items():
    print(f"{m} : {n}")


