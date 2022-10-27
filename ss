def numbers(n: int):
    if n < 0:
        return
    print(n)
    numbers(n-1)

numbers(10)

def fib(n: int):
    if n == 0 or n == 1:
        return 1
    return fib(n-1) + fib(n-2)


print(fib(10))

def power(number: int, n: int):

    if n == 2:
        return number*number

    while n > 0:
        n -= 1
        return number*power(number, n)

print(power(3, 4))


def reverse(txt: str):
    if len(txt) == 0:
        return txt

    return reverse(txt[1:])


print(reverse("Geeksforgeeks"))

def factorial(n: int):
    if n <= 1:
        return 1

    return n * factorial(n-1)


print(factorial(4))

def prime(n: int):
    if n == 1:
        return n+1

    return n/prime(n - 1)



print(prime(7))
