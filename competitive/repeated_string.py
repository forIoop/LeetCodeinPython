def repeatedString(s, n):
    a_cnt = s.count('a')
    num = n//len(s)
    mod = n%len(s)
    count = a_cnt*num + s[:mod].count('a')
    return count 
