#solutions to problem 8

def fibonacci_iterative(num = 10):
	number = 1
	prev = 0
	
	while num > 0:
		print number + prev
		num = num - 1
		prev = number
		number = number + prev	
	
#solutions to problem 9
#unfortunately I don't remember how to do this offhand :(
#I believe one would have to import the os or sys modules for this one

#Solution to problem 10
def factorial_recursive(num):
	if num > 1:
		new_num = num - 1
		factorial_recursive(new_num)
	else:
		
