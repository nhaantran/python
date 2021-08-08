# gán cho biến a giá trị là 4 với 4 là kiểu số nguyên(integers)
a=2
print(a)
#kiểu dữ liệu của a
print(type(a))

# lấy toàn bộ nội dung của thư viện decimal
# từ thư viện decimal -> import mọi thứ(*) vào

from decimal import*

# lấy tối đa 30 chữ số phàn nguyên và phần thập phân Decimal
getcontext().prec=100

print(Decimal(10)/3)



b=15
c=4
print(b//c)


import math

print(math.trunc(15/-4)) 
print (15//-4)
print('------------------------------------------------') 
complex(3,2)
i = 3 + 2j
print(i)
print(i.real)  
print(i.imag)
print(type(3 + 2j))