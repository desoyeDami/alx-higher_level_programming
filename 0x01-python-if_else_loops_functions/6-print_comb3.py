#!/usr/bin/python3
two_digits = []
for n in range(0, 100):
    if n < 99:
        if n < 10:
            n = f"0{n}"
        else:
            n = str(n)
        for i in range(len(two_digits)):
            if n[-1:0] == two_digits[i]:
                two_digits.append("")
        two_digits.append(n)
print("{}".format(two_digits), end=", ")

    # if n == 99:
    #     print("{}".format(n))
