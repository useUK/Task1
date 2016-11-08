# 12 mounth
def month (x):
	if (3<=x<=5): 
		return 'vesna'
	elif (x == 12) or (x == 1) or (x == 2):
		return 'winter' 
	elif (6<=x<=8): 
		return 'summer'
	elif (9<=x<=11): 
		return 'autmn'
	else (1<=x<=12): 
		print ('error')

x = int ( input ("Enter your value mounth:" ) )

print( month (x) ) 

