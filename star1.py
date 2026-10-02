# def star_pattern(n):
#     if(n==0):
#         return

#     print("*" * n)
#     star_pattern(n-1)

# star_pattern(5)
n=int(input("Enter a number: "))
for i in range (1, n+1):
    print("*" *i)
      