'''
a = range(5)
print(a)
print(type(a))
print(a[4])
'''
#range(start, stop[, step])
#Với cú pháp này, ta sẽ tạo một dãy số bắt đầu bằng start và kết thúc là stop – 1. Dãy số này là một cấp số cộng với công sai là 1.


'''
print(list(range(2,10,2)))
print(list(range(9,3,-1 )))
print(list(range(2,-3,-1)))
#print(list(range(999)))
a= range(99)
print(99 in a)
'''
lst= [3,(0,1,2), {'hello','hi'}]
'''i= range(len(lst))
print(i)
'''
for i in range(len(lst)):
	print(lst[i])

'''
Sự khác nhau giữa sequence scan và indexing scan
Trong bài trước, bạn thấy rằng ta không cần dùng tới hàm range vẫn có thể duyệt hết các phần tử của một List. 
Vậy điều gì khiến chúng ta đôi lúc phải dùng tới hàm range để xử lí một List?

Đó là khi ta cần update (cập nhật) List. Hãy xem hai ví dụ sau đây:
'''
'''
------------------------------------------------------------------------------
Đầu tiên là sequence scan

lst = [1, 2, 3]
for value in lst:
    value += 1
print(lst)
[1, 2, 3]

Biến variable là một biến riêng lẻ, nên không thể cập nhật được List ban đầu.
------------------------------------------------------------------------------------
'''

#Còn đối với indexing scan

lst = [1, 2, 3]
for i in range(len(lst)):
    lst[i] += 1
print(lst)
#giá trị i trỏ vào dữ liệu của lst khi dùng range(len(lst))
#Hãy lựa chọn cách sử dụng vòng lặp một cách thông minh phù hợp với mục đích của mình.

