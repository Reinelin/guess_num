maxn = input('please enter a maximum number:')
minn = input('please enter a minimum number:')
maxn = int(maxn)
minn = int(minn)

import random
r = random.randint(minn, maxn)
count = 0
while True:
	count += 1
	num = input('please enter a number:')
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
