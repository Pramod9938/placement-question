# print("Hrello World world")
# a=10
# b=20
# c=a+b
# print (c)
# use function to add two numbers
# def add_numbers(a, b):
#     print(a + b)
# add_numbers(10,20)
# n=int(input("Enter a number: "))
# if n%2==0:
#     print("Even number")
# else:
#     print("Odd number")
# def check_even_odd(n):
#     if n % 2 == 0:
#         print ("Even number")
#     else:
#         print ("Odd number")
# check_even_odd(n)

# Number positive, negative ya zero check karo.
# n=int(input("Enter a number: "))
# if n>=0:
#     print("Positive number")
# elif n<0:
#     print("Negative number")
# else:
#     print("Zero")
# def check_number(n):
#     if n > 0:
#         print("Positive number")
#     elif n < 0:
#         print("Negative number")
#     else:
#         print("Zero")
# check_number(n)
b=[1,2,3,4,5,6]
def check_largest(b):
    largest = b[0]
    for i in b:
        if i > largest:
            largest = i
    print("Largest number is:", largest)
check_largest(b)
