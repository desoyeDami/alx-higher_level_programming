def remove_char_at(str, n):
    i = 0
    res = ""
    str_len = len(str)
    while i < str_len:
        if i != n:
            res += str[i]
        i += 1
    return res
