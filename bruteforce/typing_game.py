You're in the midst of creating a typing game.

Create a function that takes in two lists: the list of user-typed words, and the list of correctly-typed words and outputs a list containing 1s (correctly-typed words) and -1s (incorrectly-typed words).

# Inputs:
User-typed: ["cat", "blue", "skt", "umbrells", "paddy"]
Correct: ["cat", "blue", "sky", "umbrella", "paddy"]

# Output: [1, 1, -1, -1, 1]

def correct_stream(user, correct):
	output = []
	for i in range(len(user)):
		if user[i] == correct[i]:
			output.append(1)
		else:
			output.append(-1)
	return output
	
