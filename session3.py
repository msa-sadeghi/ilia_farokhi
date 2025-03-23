# numbers = (1,)
# print(type(numbers))
# print(id(numbers))
# numbers += (2,)
# print(numbers)
# print(id(numbers))

# numbers = [1]
# print(id(numbers))
# numbers.append(2)
# print(id(numbers))


# numbers = {1,2,3,4,5,6,1}
# print(numbers)

# numbers = [1,2,3,4,5,1]
# print(set(numbers))
# print(len(set(numbers)))

# numbers = [1,2,3,4,5,6]
# s = 0
# for n in numbers:
#     s += n
# print(s)



# x = range(2,5)
# print(len(x))

# x = list(range(100, 201))
# print(x)
# x = list(range(100, 201,2))
# print(x)

# for i in range(100):
#     print(i, end=' ')

# from colorama import Back, Fore, Style
# print(f"{Fore.CYAN}hello{Style.RESET_ALL}")
# print(f"{Back.YELLOW}hello{Style.RESET_ALL}")

# for n in range(1, 100):
#     print(f"{Fore.CYAN}{n}{Style.RESET_ALL}", end=" ") if n % 2 == 0 else print(f"{Fore.RED}{n}{Style.RESET_ALL}", end=" ")
        

favorite_sports = {
    'sara' : 'football',
    'armin' : ['base', 'basket']
}

# print(f"armin Likes {favorite_sports['armin']}")
# print(f"sara Likes {favorite_sports['sara']}")


for item in favorite_sports:
    print(item)

for item in favorite_sports.keys():
    print(item)

for item in favorite_sports.values():
    print(item)
for item in favorite_sports.items():
    print(item)
for key, val in favorite_sports.items():
    print(key, val)

favorite_sports['nikan'] = 'football'
print(favorite_sports)

del favorite_sports['armin']
print(favorite_sports)