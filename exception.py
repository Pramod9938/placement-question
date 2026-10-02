try:
    s1=int(input("enter a number:"))
    s2=int(input("enter a number:"))
    print(s1+s2)
    
except Exception as e:
    print("Enter only valid number:",e)
    
# raise Exception("This is a custom exception message.")
# finally:
#     print("This block will always execute.")
else:
    print("No exception occurred. The sum is:", s1 + s2)