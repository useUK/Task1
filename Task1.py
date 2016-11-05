def miniCalck (x,y,z):
	float c
	if z == "+":
		c = x + y
	elif z == "-":
		c = x - y 
	elif z == "*":
		c = x * y
	elif z == "/":
		c = x / y
	else 
		print('error baka')
	c1 = round(c,2)
	return  c1
x = float(input("Enter your value 1:" ))
y = float(input("Enter your value 2:" ))
z = input("Enter your symbal:" )
answer = miniCalck (x,y,z)
print(" Your answer = ", answer) 

