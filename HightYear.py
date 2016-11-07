def hightYear (x):
	if x = 2000:
		print(x ,'is hight Year')
	elif x:
		(x // 400) != 0 ##тут типа что чисто не поделилось. И вот такая проверка ... в скобки взял на всякий случай
		print('not in this YEAR') 
	elif x:
		(x // 4) != 0 ##тут типа что чисто не поделилось. И вот такая проверка ... в скобки взял на всякий случай
		print('not in this YEAR')
	else 
		print('Yep, this is HIGHT year')

x = int(input("Enter your value year:" ))

hightYear (x)
