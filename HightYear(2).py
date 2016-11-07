def hightYear (x):
	if (x // 4) != 0:  
		if (x // 100) != 0:
			if (x // 400) != 0:
				return ('Year is normal')
	else:
		return ('Year Hight') 	 
	
x = int(input("Enter your value year:" ))

hightYear (x)
