def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisione per zero non consentita")
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as error:
    print(error)
