def removeDuplicates(nums):
    newList = []
    for i in range(len(nums)):
        if i not in newList:
            newList.append(i)

    return newList

nums = [1,2,2,3]
print(removeDuplicates(nums))
