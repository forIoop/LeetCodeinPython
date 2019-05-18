#write a function that reverses any string inputted by the user 

def reverse(string):

    reversed_string = ""
    for i in string:
      reversed_string = i + reversed_string

    print("Reversed String: " + reversed_string)

string = input("Enter any string: ")
print("Your entered string " + string)
reverse(string)
 
