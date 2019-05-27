# return the length of the last word of a phrase

def length_of_last_word(s):

    count = 0
    local_count = 0

    for i in range(len(s)):
        if s[i] == ' ':
          local_count = 0
        else:
          local_count += 1
          count = local_count
    return count


phrase = "What is the length of the last word in the sentence?"

print(length_of_last_word(phrase
