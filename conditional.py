# Syntax:
# if condition:
#      statement 1
#      statement 2
#      statement n

# age  = 17
# if age>18:
#     print("you are eligible to vote")
#     print(f"your age is {age}")   
# print("outside block of code") 


# number = 5
# if number>=5:
#     result = number**2
#     print(result)


# Syntax:
# if condition:
#     # code block to execute if condition is true
# else:
#     # code block to execute if condition is false

# user_name = "santosh"
# password = 1234
# if user_name == "santosh" and password == 12345:#False
#     print("login success")
# else:
#     print("invalid credentials")


# Syntax:
# if condition-1:  
#      statement 1 
# elif condition-2:
#      stetement 2 
# elif condition-3:
#      stetement 3 
#      ...         
# else:            
#      statement


#grading system
# marks = int(input("enter the marks: "))
# if marks>=90:
#     print(f"you got A grade you obtained {marks} marks")
# elif marks>=80:
#     print(f"you got B grade you obtained {marks} marks")
# elif marks>=70:
#     print(f"you got C grade you obtained {marks} marks")
# elif marks>=60:
#     print(f"you got D grade you obtained {marks} marks")
# elif marks>=35:
#     print(f"you got PASS grade you obtained {marks} marks")
# else:
#     print(f"you are failed you obtained {marks} marks")


    

# Syntax:
# if condition1:
#     # code block for condition1
#     if condition2:
#         # code block for condition2
#     else:
#         # code block for condition2 being false
# else:
#     # code block for condition1 being false



# user_name = input("enter username :")
# password = int(input("enter password"))
# if user_name == "santosh" and password == 12345:#False
#     print("login success")
# else:
#     print("invalid credentials")


# user_name = input("enter username :")
# password = int(input("enter password: "))
# if user_name == "vinod":
#     if password == 1234:
#         print("login success")
#     else:
#         print("invalid password")
# else:
#     print("invalid username")



# age = 17
# if age>=18:
#     print(f" you are eligible to vote {age}")
# else:
#     print(f"you are not eligible to vote ")


# Syntax:
# result = value_if_true if condition else value_if_false
# age = 17
# result = "you are eligible to vote"if age>=18 else "you are not eligible to vote"
# print(result)

age = int(input("enter your age"))
print(f"{age} you are eligble to vote") if age>=17 else print(f"you are not eligible to vote")

def age():
    return 1
age()