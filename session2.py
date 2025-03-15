# a = True
# b = False

# print(type(a))
# print(type(b))

# s = ""
# print(len(s))
# s = ' '
# print(len(s))
# s = "This is a string"
# print(len(s))

# sente = "he said don't do that"
# print(sente)
# sente = 'he said don\'t do that'
# print(sente)

# message = "he said blalalallala \nhello"
# print(message)
# message = """he said blalalallala
# hello"""
# print(message)

# number = int(input("enter a number:> "))
# if number % 2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# برنامه ای بنویس که نام کاربر را از ورودی دریافت نماید
#  در صورتی که اولین کاراکتر اسم او با
# a
# شروع شود
# ok
# not ok

# age = int(input("enter your age: "))
# if age <= 7:
#     print("baby")
# # elif 8 <= age <= 12:
# elif age >= 8 and age <= 12:
#     print("kid")
# elif 13 <= age <= 15:
#     print("teenager")
# elif 15 <= age <= 17:
#     print("junior")
# elif 18 <= age <= 50:
#     print("adult")
# else :
#     print("old")

names = ['sama', 'sara','arash']
print(f"there are {len(names)} persons in the list")
print(f"first person's name is {names[0]}")
print(f"second person's name is {names[1]}")
print(f"third person's name is {names[2]}")
new_name = input("enter a name: ")
names.append(new_name)
print(names)

names.insert(0, new_name)
print(names)
names.remove('sama')
names.pop(-1)
del names[-1]
print(names)


# برنامه ای بنویس که سه عدد از کاربر دریافت نماید و در لیستی به نام زیر اضافه کند
# numbers
# عدد اول و آخر لیست را با هم جمع کن و حاصل را نمایش بده


