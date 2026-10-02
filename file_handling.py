# with open("file.txt", "r") as f:
    #  print(f.read())
  
# st="i am a good and innocent boy"  
# f=open("file.txt", "w");
# f.write(st)
# f=open("file.txt", "a")
# f.write("\n i am a very ppositive person")
# print(f)

# Writing to a file (Warning: This overwrites existing content)
# with open("output.txt", "w") as file:
#     file.write("Hello, World!\n")
#     file.write("This is a new line.")

# Appending content safely to the end of a file
# with open("output.txt", "a") as file:
    # file.write("\nThis text is added to the bottom.")
# word=["Hello","text","bottom"]
# with open("output.txt","r")as f:
#     content=f.read()
# for i in word:
#     content=content.replace(i,"*****")
# with open("output.txt","w")as f:
#     f.write(content)
# n=int(input("Enter a number:"))
# for i in range(1,11):
#     with open("output.txt","a")as f:
#         f.write(f"{n} x {i} = {n*i}\n")
with open("file.txt", "r") as f:
     print(f.read())

st="i am a good and innocent boy" 
with  open ("file.txt", "w") as f:
    f.write(st)
with  open ("file.txt", "a") as f:
    f.write("\ i am a good and innocent boy")
    print(f)