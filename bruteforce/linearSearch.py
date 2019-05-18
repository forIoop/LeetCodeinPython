#Given an array of elements, search the one that matches up to the target

def linearSearch(list,target):

    for i in range(0,len(list)):
        if list[i] == target:
            return i


list = [2,5,8,23,4,78,20,56,25,45]
val_location = linearSearch(list,56)
print(val_location)
