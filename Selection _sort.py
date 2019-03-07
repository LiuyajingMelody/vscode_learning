

def selection_sort(newlist):
    high = len(newlist)
    array = list(range(high))
    for i in range(high):
        array[i] = max(newlist)
        newlist.remove(max(newlist))
    return array


my_list = [10, 6, 9, 4, 5, 7]
print(selection_sort(my_list))
