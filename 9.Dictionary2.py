 a= {'Na':'naananaa', (1,2): 34}
b= a.copy()
print(b)
a.clear()
print(a)
#hàm get
aa= {'Na':'naananaa', (1,2): 34}
d= aa.get('Na')
print(d)
#nếu get mà không có giá trị đó sẽ ra none
#nhưng nếu thêm 1 giá trị sau thì sẽ ra giá trị đó
e= aa.get('aaa','hi')
print(e)
f= aa.items()
print(f)
g= aa.values()
h= aa.keys()
print(g)
print(h)
'''<Dict>.pop(key [,default])
Công dụng: Bỏ đi phần tử có key và trả về value của key đó. Trường hợp key không có trong dict.
Báo lỗi KeyError nếu default là None (ta không thêm vào).
Trả về default nếu ta thêm default vào.
'''
i= aa.pop('Na')
print(i)  
m= aa.pop('aaa','a')
print(m)
o= {'heheh':65,('aa',3):3333}
n= o.popitem()
print(n)
'''<Dict>.setdefault(key [,default])
Công dụng: Trả về giá trị của key trong Dict. Trường hợp key không có trong Dict thì sẽ trả về giá trị default. 
Thêm nữa, một cặp key-value mới sẽ được thêm vào Dict với key bằng key và value bằng default.
'''
j=o.setdefault('la','aaaa')
print(j)
print(o)
'''D>.update([E, ]**F)
Công dụng: Phương thức giúp bạn cập nhật nội dung cho Dict.
F là một Dict được tạo thành bởi packing arguments (khái niệm sẽ được Kteam giải thích ở một bài trong tương lai). 
Và sẽ thêm vào Dict bằng cách
'''
a1= {'three':3,'four':4,'five':5}
a1.update(six=6,seven=7)
print(a1)
a2= {'eight':8,'nine':9}
a1.update(a2)
print(a1)
#thêm vào 1 key đã tồn tại 1 value thì value mới sẽ thay thế value cũ
b1= {'three':3,'four':4,'five':5}
b1.update(three='ba')
print(b1)
#Đây là truyền vào một E với  E có các giá chứa nhiều giá trị
c1= {'three':3,'four':4,'five':5}
c2= (['six',6],['seven',7])
c1.update(c2)
print(c1)
