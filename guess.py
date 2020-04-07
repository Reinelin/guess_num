import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1
	num = input ('please enter a number:')
	num = int(num)
	if num == r:
		print('correct!')
		print ('this is your', count, 'time(s)')
		break
	elif num > r:
		print('enter smaller')
	elif num < r:
		print('enter larger')
	print ('this is your', count, 'time(s)')
