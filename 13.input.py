#input(prompt=None)
'''Lưu ý: Có lúc bạn sẽ nhìn thấy cú pháp của nó là input(prompt=None, /). 
Cái phần thêm vào là kí tự / chỉ là một kí tự cho biết parameter prompt chỉ nhận giá trị dưới dạng positional argument. 
Nghĩa là khi bạn truyền vào cho hàm, bạn không được phép điền thêm chữ prompt.
'''

value = input() # prompt để None
print('first value is =>', value)
next_value = input('please enter one more value: ')
print('The second value is =>', next_value)

#chỉ dùng được trong CMD.....................