#Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

def roman_to_integer(s):

  rom_val = {'I': 1, 'V': 5, 'X': 10, 'L':  50, 'C': 100, 'D': 500, 'M': 1000}
  int_val = 0

  for i in range(len(s)):
      if(i > 0 and rom_val[s[i]] > rom_val[s[i-1]]):
        int_val += rom_val[s[i]] - 2*rom_val[s[i-1]]
      else:
        int_val += rom_val[s[i]]

  return int_val


roman = input("Enter a roman numeral:\n ")
print("Roman numeral as an integer: ")
print(roman_to_integer(roman))
