#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#imports functions from our stack data structure file 
from stack import Stack

#helper method checks if our open one and closed are the same
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

#can be called to check if paren are balanced
def is_paren_balanced(paren_string):
    #creates new stack object, sets balanced flag to true and starts an index that will iterate through string
    s = Stack()
    is_balanced = True
    i = 0
    #while string is still balanced it will loop through string
    while i < len(paren_string) and is_balanced:
        #current parenthesis pointer is on
        paren = paren_string[i]
        #pushes element to stack if in those value ranges case where open paren
        if paren in "([{":
            s.push(paren)
        #case where closing paren
        else:
            #returns false if only one closing paren in stack
            if s.is_empty():
                is_balanced = False
            #pops our open paren, calls helper
            else:
                #pops our open paren
                top = s.pop()
                #checks if the open paren and closed one are equal
                if not is_match(top, paren):
                    is_balanced = False
        i += 1

    #if stack is empty and balanced by default return true
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_paren_balanced("(((({}))))"))
print(is_paren_balanced("[][]]]"))
print(is_paren_balanced("[][]"))
