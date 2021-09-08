import pyautogui as py

def option1(message):
	py.moveTo(573,698)
	py.click()
	py.write(message)
	py.press('enter')

def option2():
	py.hotkey('ctrl','v')
	py.press('enter')

def option3(name):
	py.moveTo(1272,502)
	py.click()
	py.moveTo(1223,399)
	py.click()
	py.moveTo(1283,694)
	py.click()
	py.moveTo(656,261)
	py.click()
	py.write(name)
	py.moveTo(606,381)
	py.click()
	py.moveTo(832,586)
	py.click()

print('''

	███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
	██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
	███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
	╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
	███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
	╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                                              
	Created by AnonyMSAV..
	Contact --> https://t.me/Anony4790

	options --> 0 - Message spam 
		    1 - Emoji spams
		    2 - Sticker spams

	''')

options = int(input('Enter (0/1/2) : '))

if(options == 0):
	message = input('Messege : ')
	count = int(input('Count (0 = unlimited) : '))
	
	if(count == 0):
		while True:
			option1(message)
	else:
		while(0 < count):
			option1(message)
			count-=1

elif(options == 1):
	print("Type emoji in chatbox. Don't send it.")
	count = int(input('Count (0 = unlimited) : '))
	py.moveTo(573,698)
	py.click()
	py.hotkey('ctrl','a')
	py.hotkey('ctrl','c')
	py.press('enter')
	
	if(count == 0):
		while True:
			option2()
	else:
		count-=1
		while(0 < count):
			option2()
			count-=1

elif(options == 2):
	print('First send your sticker. Only unlimited sending are available.')
	name = input('Name : ')
	while True:
		option3(name)