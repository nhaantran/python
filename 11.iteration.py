a= (x for x in range(3))
print(a)
print(next(a))
print(next(a))
print(next(a))
 
#File object cũng là một iterator. Bạn cũng có thể sử dụng cách này để đọc file.

a1= [1,2,3,('ba','a')]
a2= iter(a1)
print(a2)
print(next(a2))
print(next(a2))
print(next(a2))
print(next(a2))

#Bạn cũng lưu ý, iterator này cũng dính một vấn đề như List, Dict đó chính là chỉnh một, thay đổi hai.

a3= iter('Nhân')
a4= a3
print(next(a3))
print(next(a3))
print(next(a4))
print(next(a4))

'''Hàm tính tổng – sum
Cú pháp:
sum(iterable, start=0)

Công dụng: Trả về tổng các giá trị của iterable và iterable này chỉ chứa các giá trị là số.
 Còn start chính là giá trị ban đầu. Có nghĩa là sẽ cộng từ start lên. Mặc định là 0
'''

a5= (x for x in range(3))
print(sum(a5,-1))
# sau khi sum sẽ không dùng hàm next nữa

'''Hàm tìm giá trị lớn nhất – max
Cú pháp:
max(iterable, *[, default=obj, key=func])

Công dụng: Nhận vào một iterable.Tìm giá trị lớn nhất bằng key (mặc định là sử dụng operator >).
 Default là giá trị muốn nhận về trong trường hợp không lấy được bất kì giá trị nào trong iterable.

Dấu * chính là kí hiệu yêu cầu keyword-only argument. Bạn sẽ hiểu thêm khi Kteam giới thiệu parameter trong function.
'''
b1= (x for x in range(10))
print(max(b1,default='la'))
print(max([],default='la'))
#dạng dưới không dùng default
print(max(3,4,99,234,743,3))
#hàm min tương tựu
'''Hàm sắp xếp – sorted
Cú pháp:
sorted(iterable, /, *, key=None, reverse=False)

Công dụng: Giống với phương thức sort của List object
'''
b2= {1,3,4,563,24,23423,5252,9194}
print(sorted(b2))
print(sorted(b2,reverse= True))