def fun(x):
	if x < 7:
		print('Ты учишься в детском саду', end=' ')
	elif (x < 18) and (x >= 7):
		print('Ты учишься в школе', end=' ')
	elif (x >= 18) and (x < 24):
		print('Ты учишься в ВУЗе', end=' ')
	elif (x >= 24):
		print('Ты работаешь', end=' ') 

x = int(input())
fun(x)
print(x)