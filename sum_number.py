n=int(input("Enter a number: "))
sum=0
while(n>0):
    sum+=n%10
    n//=10
print("sum of digits is:", sum)
# result=sum(map(int, str(n)))
# print("sum of digits is:", result)
