#calculate the sum of a list in python 
def sum_of_list(list) :
    total = 0

    for i in range(0, len(list)):
        total = total + list[i]

    return total

list = [2,3,6,8,2,6]
print(sum_of_list(list))
