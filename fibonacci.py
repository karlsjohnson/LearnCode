standard_input = input()
num = int(standard_input)

def fibonacci(n):
	#complete the recursive function
	if n <= 1:
		return n

	else:
		return fibonacci(n-1) + fibonacci(n-2)



for i in range(num):
	print(fibonacci(i))
