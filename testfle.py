def factorial(num):
    if num==1 or num==0 :
        return 1
    return num*factorial(num-1)

num = int(input("Enter the number of which you want to print factorial "))
result = factorial(num)
print("The factorial of the given number is",result)