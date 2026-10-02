# if( n:=len(([1,2,3,4,5,6]))>3):
#     print("The length is greater than 3")


# def status_code(code):
#     match code:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not Found"
#         case 500:
#             return "Internal Server Error"
#         case _:
#             return "Unknown Status Code"
# print(status_code(200))
# print(status_code(404))
# print(status_code(500))
# dic1 = {'a': 21, 'b': 23}
# dic2 = {'b': 24, 'c': 25}

# merged = dic1 | dic2
# print(merged)
l=[1,2,3,4,5,6]
for index, value in enumerate(l):
    print(f"Index: {index}, Value: {value}")