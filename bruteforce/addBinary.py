#Given two binary strings, return their sum (also a binary string).
#ex: a = "11", b = "1" -> "100"

def add_binary_numbers(a,b):
    #finds max length of two numbers so we know wq
    max_len = max(len(a), len(b))

    #fills numbers to the left of the max length with 0
    a = a.zfill(max_len)
    b = b.zfill(max_len)

    #initializes a result and a carry
    result = ''
    carry = 0

    #iterates through the max length of string x
    for i in range(max_len-1, -1, -1):
        #resets r after every iteration
        r = carry
        #counts the result total based on the values of x and y at each iteration
        r += 1 if a[i] == '1' else 0
        r += 1 if b[i] == '1' else 0

        #calculates if first result should be 0 or one depending on if even or odd
        result = ('1' if r%2 == 1 else'0') + result
        #calculates carry
        carry = 0 if r < 2 else 1

    #last case is for if last carry from the loop is a 1
    if carry != 0: result = '1' + result

    #returns result filled to max length to represent the fixed width
    return result.zfill(max_len)

print(add_binary_numbers('11', '1'))
