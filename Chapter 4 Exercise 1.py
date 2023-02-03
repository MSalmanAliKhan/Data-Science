# Find the greater of two numbers
a,b=input("Enter two numbers to find which is greater: ").split(",")
def greater_number(x,y):
    if x>y:
        return x
    return y
print(f"The greater number is {greater_number(int(a),int(b))}")