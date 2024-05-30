#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    liste = []
    for index in range(list_length):
        try:
            res = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            res = 0
            print("division by 0")
        except TypeError:
            res = 0
            print("wrong type")
        except IndexError:
            res = 0
            print("out of riange")
        finally:
            liste.append(res)
    return liste
