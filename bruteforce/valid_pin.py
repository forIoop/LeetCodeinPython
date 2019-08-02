ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or
exactly 6 digits. Your task is to create a function that takes a string and returns True if the PIN is
valid and False if it's not.

def is_valid_PIN(pin):
	for i in pin:
		if i.isdigit():
			continue
		else:
			return False
	
	if len(pin) == 4 or len(pin) == 6:
		return True
	
	else:
		return False
