# Add the digits of a multiple digit number
number=input("Enter a mutiple digit number ")
length=len(number)
sum=0
i=0
while i<=(length-1):
    sum+= int(number[i])
    i=i+1
print(f"The sum of the digits of {number} is {sum}\n")

num=input("Enter a multiple digit number ")
total=0
for j in num:
    total+= int(j)
print (f"The sum of digits of {num} is {total}")
