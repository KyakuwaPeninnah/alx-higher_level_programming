#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    temp = 0
    div = []
    for items in range(0, list_length):
        try:
            temp = my_list_1[items] / my_list_2[items]
        except TypeError:
            temp = 0
            print("wrong type")
        except ZeroDivisionError:
            temp = 0
            print("division by 0")
        except IndexError:
            temp = 0
            print("out of range")
        finally:
            pass
        div.append(temp)
    return div
