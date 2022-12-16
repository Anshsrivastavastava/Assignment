# # Write a Python program to count the number of even and odd numbers from a series of numbers.

x = eval(input("Enter the num :- "))
print(x)
counter_even = 0
counter_odd = 0
for i in x:
    if i%2==0:
        counter_even+=1
    else:
        counter_odd+=1
print("Number of even numbers is:-",counter_even)
print("Number of odd numbers is:-",counter_odd)

