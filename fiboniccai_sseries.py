def fiboniccai_series():
    a=0
    b=1
n=int(input())
for i in range(1, n):
  a,b=b
  b=a+b

 
cla =fiboniccai_series(a, end=" ")
print()
    
    
# n = 10
# a, b = 0, 1

# for _ in range(n):
#     print(a, end=" ")
#     a, b = b, a + b
