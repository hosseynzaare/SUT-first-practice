Num1, Num2 = map(int, input().split())
counter = 0
a = Num1
b = Num2
if Num1 > Num2:
    Num1, Num2 = Num2, Num1
my_list = [x for x in range(Num1, Num2 + 1)]
for i in my_list:
    z = 0
    for j in range(1, i + 1):
        devied = i % j
        if devied == 0:
            z += 1
    if z == 2:
        counter += 1
if a <= b:
    print("main order - amount: " + str(counter))
else:
    print("reverse order - amount: " + str(counter))
    