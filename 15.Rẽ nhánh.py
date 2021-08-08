a= 0
if a>0:
	print('a là số dương')
elif a<0:
	print('a là số âm')
else:
	print('a=0')

b= 1
if b>1:
	print('b là số dương')
elif b<0:
	print('b là số âm')
elif b==0:
	print('b=0')
elif b==1:
	print('b=1')

'''
Block trong Python
Với đa số ngôn ngữ lập trình hiện nay, thường dùng cặp dấu ngoặc { } để phân chia các block.

Riêng đối với Python lại sử dụng việc định dạng code để suy ra các block. 
Đây là điều giúp code Python luôn luôn phải đẹp mắt.

Một số điều lưu ý về việc định dạng code block trong Python:
-Câu lệnh mở block kết thúc bằng dấu hai chấm (:), 
sau khi sử dụng câu lệnh có dấu hai chấm (:) buộc phải xuống dòng và lùi lề vào trong và có tối thiểu một câu lệnh để không bỏ trống block.
-Những dòng code cùng lề thì là cùng một block.
-Một block có thể có nhiều block khác.
-Khi căn lề block không sử dụng cả tab lẫn space.
-Nên sử dụng 4 space để căn lề một block
'''

a= 345
if a//3 == 0:
	print('a là số chia hết cho 3')
elif a//3 <0:
	print('a không là số chia hết cho 3')
	if a//3 != 0:
		print('a = 345')
	else:
		print('a=0')
else:
	print('????')
