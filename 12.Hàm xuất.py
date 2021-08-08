'''

Cú pháp:
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

'''

'''
print('la','la','land',sep='.')
#khi không nhập 'end' thì nó sẽ mặc định \n
print('ka','ka',end='')
print('ka')
from time import sleep # nhập hàm sleep từ thư viện time

print('start....')
sleep(3) # dừng chương trình 3 giây
print('end...')
----------------------------------------------------------------
from time import sleep # nhập hàm sleep từ thư viện time
# in ra nội dung và kết thúc bới một chuỗi  rỗng
print('start....', end='') 
 # dừng chương trình 3 giây
sleep(3)
print('end...')
-----------------------------------
with open('Bài 21.txt', 'r+') as f:
   print('29/3/20', file=f)
with open('Bài 21.txt', 'r+') as f:
   a= f.read()
print(a)
'''
from time import sleep

your_name = "Henry"
your_great = "Hello! My name is "

for c in your_great + your_name:
    print(c, end='', flush=True)
    sleep(0.1)
print(c)

