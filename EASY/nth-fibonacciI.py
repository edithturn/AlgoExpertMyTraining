def getNthFib(n):
	first = 0
	second = 1
	if n == 0 or n == 1:
		return first

	count = 2
	nextt = first + second
	while(count < n):
		nextt = first + second
		first = second
		second = nextt
		count += 1
		print(second)
	return second
n = 6
print(getNthFib(n))