#help(open)
'''Cú pháp:
open(file, mode='r')
r / r+ / w / w+ / a / a+
'''
a= open('10.File2.txt',mode = 'r+')
print(a)
b= a.read()
a.close()
a = open('10.File2.txt',mode = 'r+')
c= a.read(10)
print(b)
print(c)
'''<File>.readline(size=-1)

Công dụng: Với parameter size thì hoàn toàn tương tự như phương thức read.

Khác biệt ở chỗ, phương thức readline chỉ đọc một dòng có nghĩa là đọc tới khi nào gặp newline hoặc hết file thì ngừng.
Con trỏ file cũng sẽ đi từ dòng này qua dòng khác.
Kết quả đọc được trả về dưới dạng một chuỗi.
Nếu không đọc được gì, phương thức sẽ trả về một chuỗi có độ dài bằng
'''

'''
Cú pháp:
<File>.readlines(hint=-1)

Ở mức độ cơ bản, ta không phải quan tâm đến parameter hint.

Công dụng: Phương thức này sẽ đọc toàn bộ file, sau đó cho chúng vào một list. 
Với các phần tử trong list là mỗi dòng của file.

Con trỏ file sẽ được đưa  tới cuối file. Khi đó, nếu bạn tiếp tục dùng readlines.
Bạn sẽ nhận được một list rỗng.
'''
data= open('10.File2.txt')
data2= data.readlines() # = list(data) = tuple(data)
print(data2)   

a1= open('10.File2.txt',mode= 'a+')
a2= a1.write('\nha')
a1.close()
print(a2)

'''
<File>.seek(offset, whence=0)
Công dụng: Phương thức này giúp ta di chuyển con trỏ từ vị trí đầu file qua offset kí tự.
Và parameter offset phải là một số tự nhiên.

Nhờ phương thức này, ta có thể ghi nội dung từ bất cứ đâu trong file.
Và từ đó ta có thể đọc lại file sau khi ta đưa con trỏ file xuống cuối file.
'''
b1= open('10.File3.txt', mode = 'r')
b2= b1.read()
b1.seek(10)
b3= b1.read()
b1.close()
print(b2)
print(b3)

'''Cấu trúc cơ bản của câu lệnh with là

with expression [as variable]:
    with-block
Nhớ rằng with-block nằm thụt vào so với dòng with expression (theo chuẩn PEP8 là 4 space và là dùng space không dùng tab)

Câu lệnh này liên quan đến phương thức __enter__ và __exit__ của đối tượng. 
Do đó, ở đây Kteam sẽ nói cơ bản khi sử dụng file.
Đặc điểm của câu lệnh with khi sử dụng với file là. Khi kết thúc with-block. File sẽ được đóng.
'''

