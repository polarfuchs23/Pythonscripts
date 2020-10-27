import random
import keyboard
posChars = " ^1234567890´°!§$%&/()=?´qwertzuiop+QWERTZUIOP*asdfghjkl#ASDFGHJKL'<yxcvbnm,.->YXCVBNM;:_@{[]}\~|"
posChars += '"'
def create(passLen=0):
    password = ""
    if passLen == 0:
        passLen = random.randint(20,25)
    for i in range(passLen):
        password += posChars[random.randint(0,97)]
    return password
print(create(int(input("Passphrase length: "))))
while not keyboard.is_pressed('esc'):
	if keyboard.is_pressed('r'):
		while keyboard.is_pressed('r'):
			pass
		keyboard.press('backspace')
		keyboard.release('backspace')
		print(create(int(input("Passphrase length: "))))