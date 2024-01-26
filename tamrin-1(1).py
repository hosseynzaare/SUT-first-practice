Number1 = int(input(""))
Number2 = int(input(""))
z = 0
for i in range(30):
    dig1 = Number1 % 2
    dig2 = Number2 % 2
    if dig1 != dig2:
        z += 1
    Number1 = (Number1 - dig1) / 2
    Number2 = (Number2 - dig2) / 2
print(z)