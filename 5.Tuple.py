''' được giới hạn bởi cặp ngoặc ()
Các phần tử của tuple được phân cách nhua bởi dấu ','
Tuple có khả năng chứa mọi giá trị
Tốc độ truy xuất tuple nhanh hơn list
Dung lượng chiếm trong bộ nhớ nhỏ hơn list
Bảo vệ dữ liệu của bạn sẽ ko bị thay đổi
có thể dùng làm key của dictionary'''

#tup= (i for i in range(10))
tup= (i for i in range(10) if i % 3 == 0)
a= tuple('Nhân')
b= tuple((1,3,4))
c= tuple(tup)

print(tup)
print(a)
print(b)
print(c)

d= ([1,2,3,4])
d += [2,3,4]
print(d)
#tương tự như toán tử nhân 
e= 0 in d
print(e)
m= len(d)
print(m)
n= d.index(2)
print(n)