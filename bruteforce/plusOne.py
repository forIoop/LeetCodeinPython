#add one to an array of integers in an array
#Example
#[1,5] -> [1,6]
#[1,9] -> [2,0]
#[9,9] -> [1,0,0]

def plus_one(digits):
    n = len(digits)

    for i in range(n-1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0

    new_number = [0] * (n+1)
    new_number[0] = 1
    return new_number

digits = [9,9,9,9,9]
print(plus_one(digits))
