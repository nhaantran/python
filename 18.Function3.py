def Nhân(T,r,a,n):
	print(T)
	print(r)
	print(a)
	print(n)
Nhân(2,3,0,8)
lst = ['238','Nhân Trần', 'BTX']
def a2(a,b,c):
	print(a)
	print(b)
	print(c)
a2(*lst)
print('------------------------')
'''Khi bạn sử dụng *, bạn không chỉ có thể unpack được các List mà bên cạnh đó bạn có thể unpack các 
container khác như Tuple, Chuỗi, Generator, Set, Dict (chỉ lấy được key).
'''
mno = (3,4,5)
dictionary = {'a': 'ba','b': 'gà','c':'LMHT'}
def btx(m,n,o):
	print(m)
	print(n)
	print(o)
btx(*mno)
btx(*dictionary)