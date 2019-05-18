#sorts elements in a list by swapping values next to each other

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
          if nums[j]>nums[j+1]:
              temp = nums[j]
              nums[j] = nums[j+1]
              nums[j+1] = temp

nums = [5,8,2,7,3,9,4,7,1,9,2,6,2,7,3,8,12,345,56,234,678,23,67,25,73,15,26,798,345]
print("\nunsorted list: ")
for i in nums:
  print(i,end=" ")

sort(nums)

print("\nsorted list: ")
for i in nums:
  print(i,end=" ")

