# while 

# 0-----------------------------------200
# 0------------------------------------

# for i in range(100):
#     print("")
# ls = []
# for i in range(100):
#     a = input("Ism kirit")
#     ls.append(a)
# print(ls)
# ps = '123456'
# for i in range(4):
#     password = input("Parolni kirit ")
#     if ps == password:
#         print("Xush kelibsiz tizimga")
#     else:
#         print("Parol xato")

# 0---
a = 4 
# while a>0:
#     print("Hello")
#     a-=1
    
# ps = '2345'
# for i in range(4):
#     password = input("Parol ")
#     if password==ps:
#         print("Xush kelibbsan")
#         break
#     else:
#         print("parol xato")

ps = '12345'
a = True
while a:
    password = input("Parol kirit ")
    if password==ps:
        print("Xush kelebsan")
        a = False
    else:
        print("Xato parol")