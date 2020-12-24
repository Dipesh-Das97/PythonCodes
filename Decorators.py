def div(a, b):
    return a/b


def decorator(func):

    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)
    return inner


div = decorator(div)

print(div(2, 4))
