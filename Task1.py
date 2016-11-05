def miniCalck (x,y,z):
	float c
	if z == "+":
		c = x + y
	if z == "-":
		c = x - y 
	if z == "*":
		c = x * y
	if z == "/":
		c = x / y
	else 
		print('error baka')
	return '%+2f' c
x = float(input("Enter your value 1:" ))
y = float(input("Enter your value 2:" ))
z = input("Enter your symbal:" )
answer = miniCalck (x,y,z)
print(" Your answer = ", answer) 

