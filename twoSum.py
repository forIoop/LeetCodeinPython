    
#Given a sorted array of integers, return two numbers such that
#they add up to a specific target, cannot use same element twice

A = [-2,1,2,4,7,11,23]
target = 13

def two_sum_array_method(A,target):
  for i in range(len(A)-1):
    for j in range(i+1, len(A)):
      if A[i] + A[j] == target:
        print(A[i], A[j])
        return True
