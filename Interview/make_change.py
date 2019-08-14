# Create a function that makes change in the most efficient way

def make_change(cents):
  nums = [25,10,5,1]
  count = 0

  for i in range(len(nums)):
   
      while cents >= nums[i]:
        cents = cents - nums[i]
        count += 1
  return count
      


print(make_change(33))
print(make_change(42))
