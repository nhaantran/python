def hsbtx(a, b):
	print('c=',a)
	print('d=',b)
hsbtx(a=99,b=100)
print('-------------')
def hsbtx(mãsố, lớp):
	print('Nhân', 'học lớp '+ lớp,'//Mã số:' + mãsố )
hsbtx('20','12A2')
def abc(name, verb):
	print('Nhân', verb + 's', name)
#Một điều nữa là bạn không được phép để positional theo sau (follow) keyword.
#abc(verb='love','eating')
abc('eating', verb='love')
print('-------------------------------------')
def math(a,b=1,c=2,d=5):
	e= (a*b) + (c*d)
	print(e)
math(a= 1) #math(1)
math(1,d=7)