def Add(x, y):
    while (y != 0):
        carry = x & y
        x = x ^ y
        y = carry << 1
        print(y)
        print(x)
        print(carry)
    return x
