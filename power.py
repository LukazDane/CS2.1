
def raise_power(a, b):
    # TODO: base case, if power is 0, answer will always be one.
    if b == 0:
        return 1
    # TODO: If power is 1 or greater, multiply input by itself, decrement power by 1, call the function again
    if b >= 1:
        return a * raise_power(a, b - 1)


print(raise_power(4, 2))
print(raise_power(5, 2))
print(raise_power(6, 2))
