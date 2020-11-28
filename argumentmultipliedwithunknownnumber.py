def mul(*args):
    result = 1
    for i in args:
        result *= i
    return result
print(mul(1,2,3))    