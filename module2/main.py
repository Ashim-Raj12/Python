# Functions

print("----- Hello I am learning functions -----")


def hello(name):
    print(f"Hello {name}")


def sum(a, b):
    sum = a + b
    print(f"The sum is {sum}")


def product(a=1, b=1):
    product = a * b
    print(f"The product is {product}")


def pallindrome(st):
    rev = ""
    for char in st:
        rev = char + rev
    if rev == st:
        print(f"{st} is pallindrome")
    else:
        print(f"{st} is not a pallindrome")


hello("Ashim")
sum(12, 54)
product(b=4, a=5)
pallindrome("NAMAN")
pallindrome("ASHIM")
