'''
Được giới hạn bởi cặp ngoặc nhọn {}, tất cả những gì nằm trong đó là những phần tử của Dict.
Các phần tử của Dict được phân cách nhau ra bởi dấu phẩy (,).
Các phần tử của Dict phải là một cặp key-value
Cặp key-value của phần tử trong Dict được phân cách bởi dấu hai chấm (:)
Các key buộc phải là một hash object
'''
a= {'Nhân': 23,'Trần': 8, '23/8': 'ngày sinh'}
print(a)
print(type(a))
#dic rỗng
aa= {}
print(aa)
print(type(aa))
b= {key:value for key,value in[('Nhân',23), ('Trần',8), ('23/8','ngày sinh')]}
print(b)
c= [('a',3),(3,'la')]
cc= dict(c)
print(cc)
print(type(c))
print(type(cc))
'''
Khởi tạo bằng keyword arguments
Cú pháp:
dict(**kwargs)

Cứ hiểu đơn giản là giống như việc bạn khởi tạo biến và giá trị rồi đưa cho dict đó giữ giùm.
Một lưu ý là những biến này không bị ảnh hưởng hoặc ảnh hưởng gì đến các biến bên ngoài
'''
m= 'qq'
n= 'cc'
o= dict(m= 23, n= 33)
print(o)
print(m)
print(n)

'''
Sử dụng Phương thức fromkeys
Cú pháp:
dict.fromkeys(iterable, value)

Công dụng: Cách này cho phép ta khởi tạo một dict với các keys nằm trong một iterable. 
Các giá trị này đều sẽ nhận được một giá  trị với mặc định là None
'''
u = ('name', 'number')
i = dict.fromkeys(u)
print(i)
#có thể thay chữ none
i = dict.fromkeys(u, 'hehe dễ mà')
print(i)

"""
Lấy value trong Dict bằng key
Cú pháp:
Your_dict[key]
"""
a1 = {'eat': 'ăn', 'sleep': 69, 'play': 'chơi'}
print(a1['eat'])
'''
Thay đổi nội dung Dict trong Python
Dict là một unhashable object. Do đó, chắc bạn cũng biết ta có thể thay đổi được nội dung nó hay không. 
Nếu bạn nào nhanh trí, chắc cũng đã biết được cách thay đổi rồi. Tương tự như List thôi!
'''
a1['eat']= 'chew'
print(a1)
# nếu mà không có thì sẽ thêm vào
a1['stupid']= 'ngu'
print(a1)
print(a1['stupid'])

a1['sleep']+= 1
#a1['sleep'] = a1['sleep'] + 1
print(a1)
a1['eat']+= " chew chew"
print(a1)