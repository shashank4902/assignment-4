#find factorial of a number
def factorial(n):
	if n==0:
		return1
	else:
		return n*factorial(n-1)
n=int(input("input a number to compute the factorial:"))
print(factorial(n))