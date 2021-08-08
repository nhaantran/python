def BTX():
	print('truong Bui Thi Xuan')
BTX()
BTX()
BTX()
BTX()
BTX()
BTX()

print('-----------------------------')
def NAME():
	pass #Lệnh pass ở trên là một lệnh “giữ chỗ” (placeholder statement) để giúp cho các block của Python không bị thiếu câu lệnh trong trường hợp bạn chưa biết viết gì cho phù hợp.
print(NAME)
print(NAME())
print('------------------------------')
def a2(parameter):
	print(parameter)
a2('hihi')
print('------------------------------')
def a6(nameage):
	print(nameage + '!')
a6('Nhan-18')
print('------------------------------')
def mobile(iphone, samsung):
	print(iphone)
	print(samsung)
mobile('iphone 12','samsung galaxy fold')

'''Khi bạn đưa default argument cho các parameter, phải để các parameter có default argument ở sau cùng.

Default argument là một unhashable container
'''
print('------------------------------')
def laptop(acer, mac='expensive'):
	print(mac)
	print(acer)
laptop('se~ mua trong tuong lai')
laptop('ngon','ngon nhung hoi mac') 
print('------------------------------')
# cai nay tuong tu cai tren
costly = '$1000'
def laptop(acer, mac=costly):
	print(mac)
	print(acer)
laptop('se~ mua trong tuong lai')
laptop('ngon','ngon nhung hoi mac') 
print('------------------------------')
def sotunhien(n= []):
	n.append(1)
	print(n)
sotunhien()
sotunhien()
sotunhien()
sotunhien()
sotunhien()
sotunhien()

