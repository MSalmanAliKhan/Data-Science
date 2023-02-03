# Find the average of three numbers
value_1,value_2,value_3=input("Enter three numbers to determine their average").split(",")
value_1=int(value_1)
value_2=int(value_2)
value_3=int(value_3)
average=(value_1+value_2+value_3)//3
print(f"The average of the three entered numbers is {average}")

#other solution
value_1,value_2,value_3=input("Enter three numbers to determine their average").split(",")
average=(int(value_1)+int(value_2)+int(value_3))//3
print(f"The average of the three entered numbers is {average}")
