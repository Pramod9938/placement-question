def greatest_number(a,b,c):
    if(a>b) and (a>c):
        return a
    elif(b>c) and (b>a):
        return b
    else:
        return c
a=int(input("enter a number: "))
b=int(input("enter a number: "))
c=int(input("enter a number: "))
print("greatest number is: ",  greatest_number(a,b,c))