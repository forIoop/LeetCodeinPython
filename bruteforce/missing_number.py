def missing_number(arr):
  sorted_arr = sorted(arr)
  for i in range(len(sorted_arr)-1):
    if sorted_arr[i] + 1 != sorted_arr[i+1]:
      return sorted_arr[i] + 1





print(missing_number([1,2,4,6,5,7,9,3]))
