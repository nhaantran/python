
'''chuỗi trần'''
print('Haizz, mình thích mấy \ngay này')
print(r'Haizz, mình thích mấy \ngay này')
#toán tử cộng
strA = "Nhân Trần\n"
strB = "lớp 12a2"
strC =  strA + "\n"+ strB
print(strC)
#toán tử nhân
strC = strA*2 + strB*2
print(strC)
#toán tử in (true hoặc false)
a = "abcdef"
b = "g"
c = b in a
print(c)
#indexing và cắt chuỗi (từ 0 đến n-1)*lưu ý nhen!
A = "abc def"
B = A[0]
C = A[-2]
print(B)
print(C)
#lấy ra phần tử cuối cùng
D= A[len(A)-1]
print(D)
#cat chuoi~
E=A[1:5]
F=A[3:len(A)]
#or F=A[3:None] or F=A[None:2] or F=A[None:] or F=A[:]
print(E)
print(F)
#cat chuoi~ nguoc lai
p=A[None:None:-1]
g=A[None:None:-2]
print(g)
print(p)
#ép kiểu dữ liệu với cú pháp "kiểu dữ liệu muốn ép ra"(giá trị muốn ép) 
q= int(6.9) #hoặc float(6) hoặc int("6")
print(q)
'''số thành chuỗi 
a= str(69) + "5"
kết quả sẽ là 695'''
#thay đổi nội dung chuỗi
ba = "HowKteam.com"
ba = ba[None:1]+ '0'+ ba[2:None]
print(ba)
print(hash(ba))