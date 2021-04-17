for i in range(1, int(input())):
	print(reduce(lambda x, y: x*10 + y, [i]*i))
