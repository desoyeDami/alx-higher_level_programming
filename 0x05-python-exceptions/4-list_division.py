#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    try:
        for n in range(0, list_length):
            try:
                element_1 = my_list_1[n] if n < len(my_list_1) else None
                element_2 = my_list_2[n] if n < len(my_list_2) else None

                if element_1 is None or element_2 is None:
                    raise IndexError("out of range")
                if not (isinstance(element_1, (int, float)) and
                        isinstance(element_2, (int, float))):
                    raise TypeError("wrong type")
                if element_2 == 0:
                    raise ZeroDivisionError("division by 0")
                result.append(element_1 / element_2)

            except IndexError:
                result.append(0)
                print("out of range")
            except ZeroDivisionError:
                result.append(0)
                print("division by 0")
            except TypeError:
                result.append(0)
                print("wrong type")
    finally:
        return result
