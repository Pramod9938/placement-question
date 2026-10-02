# n=1232
# reverse_number=0
# while(n>0):
#     reverse_number=reverse_number*10+n%10
#     n//=10
#     print("Reverse of the number is:", reverse_number)
n=int(input("Enter a number: "))
reversed_number=0
print(int(str(n)[::-1]))