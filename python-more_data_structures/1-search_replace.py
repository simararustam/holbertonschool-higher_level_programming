#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list[:]
    for i in range(len(new)):
        if new[i] == search:
            for j in range(len(new)):
                if new[j] == replace:
                    temp = new[i]
                    new[i] = new[j]
                    new[j] = temp
            return new
