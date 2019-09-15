GUEST_LIST = {
	"Randy": "Germany", 
	"Karla": "France", 
	"Wendy": "Japan", 
	"Norman": "England", 
	"Sam": "Argentina"
}

def greeting(name):
	for guestName in GUEST_LIST:
		if guestName == name:
			return  "Hi! " + "I'm " + guestName + ", and I'm from " + GUEST_LIST[name] + "."
	return "Hi! I'm a guest."
