#Construct a sequence that starts at 1, counts the amount of numbers in that sequence
#Then conunt that output number
#Given an integer n, determine the nth term in our count and say sequence

def next_term(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1
        result.append(str(count) + s[i] )
        i += 1
    return ''.join(result)
s = "1211"
print(next_term(s))
