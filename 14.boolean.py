print(3*3 >= 27 & 3>=1)
#print(0==(-1+3)*2)
print((5*0) != 0)
'''
Lưu ý: Python so sánh các kí tự với nhau bằng cách đưa chúng về dưới dạng số bằng hàm ord.
 Bạn có thể tham khảo giá trị của nó trong ASCII Table.
'''
#print('K' == 'T')
print('Trần' == 'Trần')
print(ord('a'))
print(ord('A'))
#Còn nếu bạn dùng các toán tử như >, <, != thì nhiều lúc Python sẽ không cần phải đi hết các giá trị iterable. 
#Nếu như ở vị trí i nào đó mà đã hai giá trị không bằng nhau thì nó sẽ dừng lại.
print('a' > 'ABC')
print('aaa'< 'aaA')
print('aaa'> 'aaaAAAAA')
'''
--------------------------
'''
a= [1,2,3]
b= [1,2,3]
print(a == b)
print(a is b)
a=b
print(a is b)
'''
Từ đây, ta có thể suy ra một kết luận. 
Khi so sánh hai giá trị (đối tượng) bằng toán tử == thì Python sẽ so sánh bằng giá trị của chúng.
Còn nếu so sánh bằng toán tử is thì Python sẽ lấy giá trị của hàm id để so sánh.
___________________________________________________________________________________________________
Lưu ý khi dùng toán tử is
Không nên so sánh 2 số chẳng hạn 699 = 699 => kết quả sẽ luôn là True
a= 6 / b= 6 thì kết quả sẽ ra False.
Nhưng có 1 số trường hợp:
>>> a = -5
>>> b = -5
>>> a is b
True
>>> c = 256
>>> d = 256
>>> c is d
True
>>> a = 'abc'
>>> b = 'abc'
True
---------------------------
Các số từ -5 đến 256 hoặc là một số chuỗi có số kí tự dưới 20 thì các biến có cùng một giá trị sẽ có 
cùng một giá trị trả về từ hàm id.
'''

'''Thật vậy, các giá trị đều là các boolean. 
Và đương nhiên, bạn có thể chuyển đối chúng thành các Boolean bằng hàm bool.
Mọi giá trị khi chuyển về Boolean đều là True trừ một số trường hợp sau

Số 0
None
Rỗng
'''
print(bool(1))
#  0 là False
#  1 là True
print(False +1)
print(True  +1)   

'''
Nếu bạn từng học một số ngôn ngữ lập trình khác. 
Bạn đôi lúc phải kiểm tra những trường hợp như kiểu tra một số n có nằm trong khoảng (a; b), đoạn [a; b],
nửa khoảng (a; b], nửa khoảng [a; b) hay không?
hoặc là kiểm tra xem một số k có bằng một trong những số nhưx, y hoặc z hay không.
Đương nhiên, những lần làm như vậy cũng làm bạn hơi cực

>>> n = 5
>>> n > 1 and n < 6 # kiểm tra xem n có nằm trong khoảng (1; 6) hay không
True
>>> n > 1 and n < 4 # kiểm tra xem n có nằm trong khoảng (1; 4) hay không
False

Nhưng với Python, bạn có thể làm thế này.

>>> 1 < a < 6
True
>>> b = -4
>>> b < -3 < -1 < 0 < a < 6 # thậm chí là dài như thế này
True
--------------------------------------------------------
Với trường hợp nếu bạn muốn kiểm tra xem một số k có bằng x hoặc y hoặc là z hay không
thì thường bạn phải viết khá dài.

>>> k = 4
>>> k == 3 or k == 4 or k == 5
True
'''
k= 4
print(k in (3,4,5))