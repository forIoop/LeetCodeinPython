# Returns floor of square root of x
def floorSqrt(x) :
  #base case for the square root of 0 or 1
  if (x == 0 or x == 1):
    return x
    # Binary search method for finding the square root
  start = 1
  end = x
  while (start <= end) :
         mid = (start + end) // 2

         # case where x is a perfect square
         if (mid*mid == x) :
             return mid

           # Since we need floor, we update
          #answer when mid*mid is smaller
         #  than x, and move closer to sqrt(x)
         if (mid * mid < x) :
             start = mid + 1
             ans = mid

         else :

             # If mid*mid is greater than x
             end = mid-1

  return ans
  
print(floorSqrt(2))
print(floorSqrt(9))
print(floorSqrt(243))
