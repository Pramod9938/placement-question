# n=23133343
# print(str(n)[::-1])



def reverse_number(n):
    if((n<0)):
        sign = -1
    else:
        sign = 1
    return sign * int(str(abs(n))[::-1])

n=int(input("Enter a number: "))
print(reverse_number(n))