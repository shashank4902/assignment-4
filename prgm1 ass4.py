#To find maximum of numbers
a=float(input("please enter thefirst value"))
b=float(input("please enter the first value"))
c=float(input("please enter the first value"))
if (a>b and a>c):
	print("{0} is greater than both {1} and{2}".format(a,b,c))
elif(b>a and b>c):
	print("{0} is greater than both {1} and {2}".format(b,a,c))
elif(c>a and c>b):
	print("{0} is greater than both {1} and {2}".format(c,a,b))
else:
	print("either any two values or all the three values are equal")