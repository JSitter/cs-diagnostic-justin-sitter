#solutions to problem 8

def fibonacci_iterative(num = 10):
	number = 1
	prev = 0
	
	while num > 0:
		print number + prev
		num = num - 1
		prev = number
		number = number + prev	
	
	
