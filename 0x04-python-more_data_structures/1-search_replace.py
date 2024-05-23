#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if search in my_list:
        my_liste = [i if i != search else replace for i in my_list]
        return my_liste
    return my_list
