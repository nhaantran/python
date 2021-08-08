def kteam(pos_or_key_arg, *, key_arg1, key_arg2):
	print(pos_or_key_arg)
	print(key_arg1)
	print(key_arg2)
kteam(1, key_arg1=2, key_arg2='Kteam')
lst = [0,100,999]
def a(*,b,c):
	print(b)
	print(c)
a(*('a','b','c'),'d')