 # giới hạn bởi 1 cặp ngoặc vuông []
 # các phần tử của list cách nhau bởi dấu ','
 # List có khả năng chưa mọi giá trị đối tượng của Python và bao gồm chính nó.
 # a= [] list rỗng

a= [1,3,'la',]
b= [[[3,2],[3,3]],[['la','la','land']],[2222]]
print(a)
print(b)
c= [i for i in range(23)]
print(c)
d= [[n,n*5,n*10]for n in range(4)]
print(d)
e= list('Nhân Trần')
print (e)
#  a = a  + sth có thể được viết tắt bằng a  += sth (cùng kiểu dữ liệu mới cộng được)
m= [23,8]
m+= ['Nhân','Trần']
m*= 3
#không thể nhân 2 list với nhau
print(m)
n= 3 in m
print(n)
q= [22,33,44,55,[3,2]]
#w= q[3]
#w= q[3][1]
w= q[1:4]
#lấy ra toàn bộ và đảo ngược lại w=q[::-1]
print(w)
'''thay đổi giá trị của biến 
l= [3,4,5,6,7,8]
l[2]= 'lêu lêu'
print(l)
'''
u=[1,2,3]
#b = a
k= list(a)
#b[0]= 'adadadada'
b[0]= 'adadadadada'
print(a)
print(b)

o= [[1,2,3],[4,5,6]]
i= list(list(o))
print(i)
print(o)
i[0][0]= 9999999999999
print(i)
print(o)
#thay đổi 1 phàn tử  trong list con thì sẽ thay đổi theo còn thay 1 list thì không có vấn đề gì
'''
o= [[1,2,3],[4,5,6]]
i= list(list(o))
print(i)
print(o)
i[0]= 9999999999999
print(i)
print(o)
'''

