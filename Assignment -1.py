#------------------Write a Python program to get the Fibonacci series between 0 to input--------------------

num_1 = 0
num_2 = 1
fibonacci = 0
input_num = int(input("Enter your num:-"))
for i in range(0,input_num):
    print(fibonacci,end=" ")
    num_1=num_2
    num_2=fibonacci
    fibonacci=num_1+num_2

