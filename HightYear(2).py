def hightYear (x):
	if (x // 4) != 0:  
		if (x // 100) != 0:
			if (x // 400) != 0:
				return ('str(x) - не високосний') ## return (x '- не висококосний')
	else:
		return ('Fail') 	 
	
x = int(input("Enter your value year:" ))

hightYear (x)
