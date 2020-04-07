import random
r = random.randint(1, 100)
while True:
	num = input ('please enter a number:')
	num = int(num)
	if num == r:
		print('correct!')
		break
	elif num > r:
		print('enter smaller')
	elif num < r:
		print('enter larger')
