#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1
    import sys
    arg = sys.argv
    if len(arg) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = arg[2]
    first_num = int(arg[1])
    second_num = int(arg[3])
    if operator == "+":
        res = calculator_1.add(a=first_num, b=second_num)
    elif operator == "-":
        res = calculator_1.sub(a=first_num, b=second_num)
    elif operator == "*":
        res = calculator_1.mul(a=first_num, b=second_num)
    elif operator == "/":
        res = calculator_1.div(a=first_num, b=second_num)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print(f"{first_num} {operator} {second_num} = {res}")
