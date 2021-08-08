#for variable_1, variable_2, .. variable_n in sequence: 
    
a= (x for x in range(3))
for b in a:
	print('->',b)

a1={'Name:':'Nhân Trần','Age:': 18}
for key, value in a1.items():
	print(key,value)

a2='Nhân Trần'
for name in a2:
	if name == ' ':
		break
	else:
		print(name)
'''		
a2='Nhân Trần'
for name in a2:
	if name == ' ':
		continue
	else:
		print(name)

'''
