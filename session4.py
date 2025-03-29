# all_students = {
#     'sara' : 100,
#     'nikan' : 100,
#     'armin' : 85
# }
# print(f"artin's score is {all_students.get('artin')}")
# try:
#     print(f"artin's score is {all_students['artin']}")
# except KeyError:
#     print("not found")

# for student in all_students:
    # print(f"{student}'s score is {all_students[student]}")
    # print(f"{student}'s score is {all_students.get(student)}")
    


numbers = [1,2,31,14,65,6]
# s = 0
# for n in numbers:
#     s += n % 10
# print(s)
# s = 0
# i = 0
# while i < len(numbers):
#     s += numbers[i] % 10
#     i += 1
# print(s)

# s = 0
# while True:
#     n = int(input("enter a number:> "))
#     s += n
#     if input('do you want to exit? y or n: ').lower().startswith('y'):
#         break
# print(s)
# running = True
# s = 0
# while running:
#     n = int(input("enter a number:> "))
#     s += n
#     if input('do you want to exit? y or n: ').lower().startswith('y'):
#         running = False
# print(s)


# for i in range(1,3):
#     if i % 2 == 0:
#         break
#     print(i)
# else:
#     print("blalalalla")

# for i in range(3):
#     if i % 2 != 0:
#         continue
#     print(i)


def my_function(name, family):
    return f"hello {name} {family}"


print(my_function('sara', 'blalal'))

def is_even(number):
    if number % 2 == 0:
        return True
    
    return False

print(is_even(12))
print(is_even(13))