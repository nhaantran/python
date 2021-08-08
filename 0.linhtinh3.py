'''
tup = (1, 2, [3, 4])
tup[2] += [50, 60]
print(tup)'''
#a= [1,2,3,4,5]
#a[2]+= 3
#print(a)
''';
b1= open('file3.txt', mode = 'r')
b2= b1.read()
b1.seek(0)
b3= b1.read()
b1.close()
print(b2)
print(b3)
'''
from time import sleep # nhập hàm sleep từ thư viện time
# in ra nội dung và kết thúc bới một chuỗi  rỗng
print('start....', end='') 
 # dừng chương trình 3 giây
sleep(3)
print('end...')

