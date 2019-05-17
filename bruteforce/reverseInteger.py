#write a function that reverses any integer inputted by the user

def reverse(n):

    d = 0
    rev = 0

    if(n<0):

        neg = abs(n)
        while(neg>0):
          d = neg%10
          neg= int(neg/10)
          rev = rev*10 + d

    return rev*-1


    while(n>0):
        d = n%10
        n = int(n/10)
        rev = rev*10 + d

    return rev



x = int(input("Please enter an integer: "))
r = reverse(x)
print("Your integer: " + str(x))
print("Your integer reversed: " + str(r))


