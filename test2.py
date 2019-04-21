# # 1. Function
# def to_hour(minute, seconds=10000): #custom function creation, default arguments shuld be at last
#     hour = minute/60 + seconds/3600
#     return hour
# min = float(input("Whats the min: "))
# sec = float(input("Whats second:"))
# print(to_hour(min,sec)) #function invocation

# # 2. Condition Block
# # if
# a = float(input("Enter a Number:"))
# if a<5:
#     print("less than 5")
# elif a == 5 :
#     print("equal to 5")
# else:
#     print("greater than 5")
# # for
# data = ["debasis","subhasis", "runu"]
#
# for name in data:
#     if "sis" in name:
#         print(name)
#
# # while loop with if
# # multi dimensional for loop
# # joining list for multi dimension for LookupError
# name = ['deba', 'runu','subha','manju'];
# surname = ['maity', 'samanta', 'maity', 'maiti']
# fullname = zip(name, surname)
# for i, j in fullname:
#     print(i+" " + j)
# password = "";
# while password != "!pass":
#     password = input("Enter Password")
#     if password == "!pass":
#         print("You are logged in")
#     else:
#         print("Enter Password Again")
