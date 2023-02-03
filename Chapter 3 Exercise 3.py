# Find the sum of natural numbers upto a user defined limit
Natural_number=int(input("Enter the natural number upto which the sum is to be done"))
if Natural_number==0 or Natural_number<=0:
    print ("Enter a natural number i.e greater than zero and not in decimal")
sum=0
i=1
while i <= Natural_number:
    sum=sum+i
    i=i+1
if sum>0:
    print (f"The sum of natural numbers is {sum}")

