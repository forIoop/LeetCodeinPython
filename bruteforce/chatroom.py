Write a function that returns the number of users in a chatroom based on the following rules:

If there is no one, return "no one online".
If there 1 person, return "[user1] online".
If there are 2 people, return [user 1] and [user 2] online".
If there are n>2 people, return the first two names and add "and n-2 more online".
For example, if there are 5 users, return: "[user1], [user2] and 3 more online"

def chatroom_status(users):
	if len(users) == 0:
		return "no one online"
	if len(users) == 1:
		return users[0] + " online"
	if len(users) == 2:
		return users[0] + " and " + users[1] + " online"
	
	else:
		return users[0] + ", " + users[1] + " and " + str((len(users)-2)) + " more " +"online"
