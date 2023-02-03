# Create a generator that prints even numbers upto a certain limit.
def num(n):
    for i in range(1,n+1):
# for i in range(2,n+1,2): can also be used here 
     if i%2==0:
        yield(i)

numbers = num(10)
for j in numbers:
    print(j)
for j in numbers:
    print(j)
