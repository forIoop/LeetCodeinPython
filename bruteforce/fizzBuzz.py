#Write a program that outputs the string representation of numbers from 1 to n.
#But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

def fizzBuzz(n):

  if n < 1:
        return []

  for i in range(1,n+1):
        if i%3 == 0 and i%5 == 0:
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(str(i))


n = int(input("Give me a number: \n"))

print(fizzBuzz(n))
