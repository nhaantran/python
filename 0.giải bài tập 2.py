#Nhập từ bàn phím 3 số, in ra số lớn nhất (cố gắng ít dòng code nhất có thể - ở đây không tính việc nhập dữ liệu)

a = '238'

if a[0]>a[1] & a[0]>a[2]:
	print(a[0],' là số lớn nhất trong a')
elif a[1]>a[0] & a[1]>a[2]:
		print(a[1],' là số lớn nhất trong a')
elif a[2]>a[1] & a[2]>a[0]:
		print(a[2],' là số lớn nhất trong a')
else:
	print('3 số bằng nhau')