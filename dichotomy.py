
import math


def binary(list, item):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = math.floor((low+high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess <= item:
            low = mid+1
        else:
            high = mid+1
        return None


my_listing = [1, 2, 3, 4, 5, 6, 7]
print(binary(my_listing, 4))
