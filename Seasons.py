# 12 mounth
def month (x):
	if x <= 12 or x <= 1:
		print ('There are only 12 mounth')
		break	
		if (x == 12) or (x == 1) or (x == 2):
			return 'winter'
			break 
		if (x == 6) or (x == 7) or (x == 8):
			return 'summer'
			break
		if (x == 9) or (x == 10) or (x == 11):
			return 'autmn'
			break
	else: 
		return 'vesna'
		break

x = int ( input ("Enter your value mounth:" ) )

print( month (x) ) 

