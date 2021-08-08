a = 'My team is %s'%('the best')
print(a)
ab = 'Try %s by %s'%('one','one')
print(ab)
s= '%s + %s = %s'
result = s %('1','1','2')
print(result)
g ='3312%d' %(10)
print(g)
f= '3%f'%(14.3)
print(f)
#%.'1 con so nao do thi se hien thi ra bao nhiu so o phan thap phan'f %()
ff = '%.1f'%(34.45)
print(ff)
hello = 'My name'
ket = f'{hello} is Nhan Tran'
print(ket)
name= ''
age='18'
adress='HCM city' 
ketqua= f'Student info: {{name}}\n{age}\n{adress} '
print(ketqua)
la= '3:{ba}, 2:{ba}'.format(one=123, ba=456)
print(la)
'''{:(c)<n}: can le` trai
{:(c)>n}: can le` phai
{:(c)^n}: can giua~
'''
r= 'My class is {:.^100} BTX'.format('12a2')
print(r)

# phần định dạng
row_1 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)