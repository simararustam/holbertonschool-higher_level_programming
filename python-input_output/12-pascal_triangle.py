#!/usr/bin/python3
"""Pascal Triangle"""


def pascal_triangle(n):
    """Determine pascal triangle"""
    if n <= 0:
        return list

    curr_list = [1]
    temp_list = []
    pascal_tri = []

    for i in range(n):
        temp_list.append(1)
        for j in range(1, len(curr_list)):
            temp_list.append(curr_list[j] + curr_list[j - 1])
        temp_list.append(1)

        pascal_tri.append(curr_list)
        curr_list = temp_list
        temp_list = []
    return pascal_tri
