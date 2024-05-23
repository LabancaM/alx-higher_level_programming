#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    liste2 = []
    for i in matrix:
        liste = [j ** 2 for j in i]
        liste2.append(liste)
    return liste2
