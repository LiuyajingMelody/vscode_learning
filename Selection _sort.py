

def selection_sort(newlist):
    high = len(newlist)
    array = list(range(high))
    for i in range(high):
        array[i] = max(newlist)
        newlist.remove(max(newlist))
    return array


def findmaxindex(importarray):
    high1 = len(importarray)
    maxarray = importarray[0]
    maxarray_index = 0
    for i in range(high1):
        if maxarray <= importarray[i]:
            maxarray = importarray[i]
            maxarray_index = i
    return importarray[maxarray_index]  


my_list = [10, 6, 9, 4, 5, 7]
print(findmaxindex(my_list))
print(selection_sort(my_list))
