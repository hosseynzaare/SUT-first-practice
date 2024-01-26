def dec_to_bin(num):
    """convert decimal number to binary number with 32 part in list
    """
    list = []
    while (num > 0):
        rem =int(num % 2)
        list.append(rem)
        num =(num - rem) / 2
    while len(list) < 32:
        list.append(0)
    list.reverse()
    return list
number1 = int(input())
number2 = int(input())
list1 = dec_to_bin(number1)
list2 = dec_to_bin(number2)
list = list2 + list1
test_case = int(input())
count = 0
while test_case > count:
    test = int(input())
    if test < 32:
        if list[-test - 1] == 1:
            print("yes")
        else:
            print("no")
    else:
        if list[63 - test] == 1:
            print("yes")
        else:
            print("no")
    count += 1
