#Uses mid element to narrow array value down until found
import random

def binarySearch(list,element):
    list.sort()
    top = len(list)
    bottom = 0

    while top > bottom:
            middle = (top + bottom) // 2
            if element == list(middle):
                return middle
            elif element < list[middle]:
                top = middle
            elif element > list[middle]:
                bottom = middle

    return -1

list = [int(1000*random.random()) for i in range (1000)]
print(binarySearch,list,list[random.randrange(0, len(list))]
