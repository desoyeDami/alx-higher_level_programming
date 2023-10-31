def uppercase(str):
    for s in str:
        if 97 <= ord(s) <= 122:
            print(chr(ord(s) - 97 + 65), end= "")
        else:
            print(s, end="")