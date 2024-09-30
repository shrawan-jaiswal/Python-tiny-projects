# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("java", "Python")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)


# def check_word():
        
#     word = "learning"

#     with open("practice.txt", "r") as f:
#         data = f.read()
#         if (data.find(word) != -1):
#             print("Found")
        
#         else:
#             print("Not Found")


# check_word()


# def check_for_line():
#     word = "learning"
#     data = True
#     line_no = 1
#     with open("practice.txt", "r") as f: 
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# check_for_line()


# def check_line():
#     word = "pyq"
#     data = True
#     line_num = 1
#     with open("practice.txt", "r") as f:
#         while data:
#             data = f.readline()
#             if (word in data):
#                 print(line_num)
#                 return
#             line_num +=1
#     return -1

# print(check_line())


# with open("practice.txt", "w") as f:
#     data = f.write("Hello world")
#     data = f.write("I really love python\n")
#     data = f.write("I really love Cybersecurity\n")

#     print(data)

# with open('practice.txt', 'w') as file:
#     lines = ["shrawan is new don\n", "234123\n", "I love cybersecurity\n"] #here we are inserting a whole list inside a txt file
#     file.writelines(lines)
#     file.write("Third line\n")
#     file.write("Fourth line")

# with open("practice.txt", "a") as f:
#     appndTxt = f.write("\nHello again!!!")
#     print(appndTxt)

# with open("practice.txt", "r") as f:
#     appndTxt = f.read()
#     print(appndTxt)

# with open("practice1.txt", "x") as f: # x mode creates new file like we created new practice1 file here
#     appndTxt = f.write("hello world")
#     print(appndTxt)
    
# import os


# if os.path.exists("My_text.txt"):
#     print("file exists")
# else:
#     print("file doesnot exists")



import os
os.remove("demo.txt")