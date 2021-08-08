'''
Được giới hạn bởi cặp ngoặc {}, tất cả những gì nằm trong đó là những phần tử của Set.
Các phần tử của Set được phân cách nhau ra bởi dấu phẩy (,).
Set không chứa nhiều hơn 1 phần tử trùng lặp
Set chỉ có thể chứa các hashable object nhưng chính nó không phải là một hashable object. Do đó, bạn không thể chứa một set trong một set.
'''
#list là 1 unhashable và tuple là 1 hashable
set1= {69,96}
print(set1)
set2={'lala'}
print(set2)
set3= {('a',3)}
print(set3)
'''a= (3,4)
print(hash(a))'''
set4= {'Nhân trần', 'Nhân', 38}
print(set4)
set5= {1,1,1,1}
print(set5)
set6= {}
print(set6)
print(type(set6))
set7= {(n,n+1,n+2) for n in range(3)}
print(set7)
set8= set(('aaaaaabbbccc'))
print(set8)
set9= set()
#cách tạo ra set rỗng
print(set9)
print(type(set9))
print(4,3 in {1,2,3})
print({1,2,3,4,5,6,7,8,9}-{1,2,3,4,5,6,7})
#cách tạo ra set rỗng
set10= {1,2}-{1,2}
print(set10)
print(type(set10))
#có thể tạo ra set rỗng bằng cách này
print({1,2,3,4,5,6}&{5,6,7,8,9}) #toán tử và
print({1,2,3,4,5,6}|{5,6,7,8,9}) #toán tử hoặc
'''toán tử 
{}^{}
'''
set_1= {11,12,13}
set_2= {13,14}
set_3= set_1&set_2
set_4= set_1|set_2
set_5= set_4-set_3
print(set_3)
print(set_4)
print(set_5)
print(set_1^set_2)
#set_5 = set_4 - set_3  =  set_1 ^ set_2
#cách tạo ra set rỗng
set_5.clear()
print(set5)
set_1.pop()
print(set_1)
set_1.remove(13)
print(set_1)
# .remove()      Công dụng: Loại bỏ giá trị value ở trong Set. Nếu như value không ở trong Set, thông báo lên lỗi KeyError.

# .discard()     Công dụng: Loại bỏ giá trị value ở trong Set. Nếu như value không ở trong Set, thì sẽ bỏ qua.
set_2.discard(15)
print(set_2)
set_6 =set_1.copy()
print(set_1)
print(set_6)
set_6.add(3)
print(set_6)
print(id(set_6))
set_6.add(122)
print(id(set_6))
# => set ko phải là hash object => set là 1 unhashable