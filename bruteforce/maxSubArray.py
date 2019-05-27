    
#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
data = [1,2,3,-9,5,7,-99,2,8]  #Answer should be 12

def max_sub_array(arr):
  global_max = 0
  for x in range(len(data)+1):
        for j in range(len(data)+1):
            if data[x:j]:
             current_max = sum(data[x:j])
             if current_max > global_max:
                global_max = current_max
  return global_max


print(max_sub_array(data))
