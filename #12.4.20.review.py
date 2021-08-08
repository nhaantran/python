waytosucceed= ['learn','relax','enjoy','experience']
print('These are the steps to help you succeed')
for steps, advice in enumerate(waytosucceed,1):
    print(steps,'is', advice)
print('------------------------------------------------')
List = ['avocado','sweet potato','salmon','chocolate','rice','broccoli']
Lst= [a.capitalize() for a in List] 
print('Foods that I\'d love to eat eat on a regular basis:')
from time import sleep
for numbers, foods in enumerate(Lst,1):
	print(numbers,'. ',foods,sep='')
	sleep(0.5)
