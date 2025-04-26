# def mul(*numbers):
#     """
#     Multiplies all numbers in a list.
    
#     Args:
#         numbers (list): A list of numbers.
        
#     Returns:
#         int: The product of all numbers in the list.
#     """
#     print(numbers)
#     print(type(numbers))
#     result = 1
#     for number in numbers:
#         result *= number
#     return result

# print(mul(1, 2, 3, 4))  # Output: 24



# def greet(name, family, _class="python"):
#     return f"hello {name} {family} welcome to python {_class}"
# def greet(**kwargs):
#     """
#     Greets a person with their name, family, and class. 
#     """
#     name = kwargs.get("name", "")
#     family = kwargs.get("family", "") 
#     _class = kwargs.get("_class", "")
#     return f"hello {name} {family} welcome to python {_class}"


# print(greet(name="sara", family="family1"))
# print(greet(family="family2", name="arad", _class="java"))


"""
اسم
فامیلی
سن

اگر سن بزرگتر از 18 بود
    بزرگسال هستید
اگر سن بزرگتر از 12 بود و کوچکتر از 18 بود
    نوجوان هستید                    

"""

# name = "amir"

# with open("test.txt", "a") as f:
#     f.write(name + "\n")


# with open("test.txt", "r") as f:
#     name = f.read()
#     print(name)
