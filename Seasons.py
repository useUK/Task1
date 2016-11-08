# 12 mounth
def month (x):
	if (1<=x<=12): 
		
		print ('There are only 12 mounth')	
		
		if (x == 12) or (x == 1) or (x == 2):
			return 'winter' 
		if (6<=x<=8): 
			return 'summer'
		if (9<=x<=11): 
			return 'autmn'
		else: 
		return 'vesna'

x = int ( input ("Enter your value mounth:" ) )

print( month (x) ) 

