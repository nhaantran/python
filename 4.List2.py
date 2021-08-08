a= [1,2,1,4,5,6,7]
b= a.count(2)
print(b)
c= a.index(1)
print(c)
d= a.copy()
print(d)
print(a)
d[0]= 'la'
print(d)
print(a)
#copy là tạo ra 1 cái mới. không thay đổi cái cũ
e= a.clear()
print(a)
print(e)
a.clear()
print(a)
a.append(4)
print(a)
a.append([5,6,7])
print(a)
a.extend([[23,8],9])
print(a)
a.extend(['la'])
print(a)
#insert: thêm phần tử x vào vị trí y // a.insert(y,x)
a.insert(2,'la')
print(a)
#pop: lấy ra phàn tử thứ y // a.pop(y)
#khi không nhập y --> sẽ tự động lấy ra phần tử cuối cùng
print(a.pop(4))
#không có gán 
a.remove(4)
print(a)
p= a.remove('la')
print(p)
a.reverse()
print(a)
g= [1,3,2,7,5]
g.sort()
print(g)
'''Chúng ta sẽ nói đến từ khóa reverse. Từ khóa này bạn chỉ có thể cho 2 giá trị, một là True, hai là False.

Nếu là False, các phần tử được sắp xếp từ bé đến lớn, còn ngược lại là từ lớn đến bé.'''
i= [1,4,6,8,2,3]
i.sort(reverse=False)
print(i)