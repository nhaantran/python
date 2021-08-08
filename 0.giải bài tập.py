#bài 7
#a = "\" không hợp lệ
#a= “””asd34’asdfjoaisdfadf””” không hợp lệ

#bai` 9 
# phần định dạng
row_1 = '+ {:_<6} + {:_^15} + {:_>10} +'.format('', '', '')
row_2 = '| {:<6} | {:^15} | {:>10} |'.format('ID', 'Ho va ten', 'Noi sinh')
row_3 = '| {:<6} | {:^15} | {:>10} |'.format('123', 'Yui Hatano', 'Japanese')
row_4 = '| {:<6} | {:^15} | {:>10} |'.format('6969', 'Sunny Leone', 'Canada')
row_5 = '+ {:_<6} + {:_^15} + {:_>10} +'.format('', '', '')

# phần xuất kết quả
print(row_1)
print(row_2)
print(row_3)
print(row_4)
print(row_5)

row = '+ {:_<6} + {:_^15} + {:_>10} +\n| {:<6} | {:^15} | {:>10} |\n| {:<6} | {:^15} | {:>10} |\n| {:<6} | {:^15} | {:>10} |\n+ {:_<6} + {:_^15} + {:_>10} +'.format('', '', '','ID', 'Ho va ten', 'Noi sinh','123', 'Yui Hatano', 'Japanese','6969', 'Sunny Leone', 'Canada','', '', '')
print(row)
print('+ {:-<6} + {:-^15} + {:->10} +\n'.format('', '', '') + '| {:<6} | {:^15} | {:>10} |\n'.format('ID', 'Ho va ten', 'Noi sinh') + '| {:<6} | {:^15} | {:>10} |\n'.format('123', 'Yui Hatano', 'Japanese') + '| {:<6} | {:^15} | {:>10} |\n'.format('6969', 'Sunny Leone', 'Canada') + '+ {:-<6} + {:-^15} + {:->10} +'.format('', '', ''))
print('+ {:-<6} + {:-^15} + {:->10} +\n'.format('', '', '') + '| {:<6} | {:^15} | {:>10} |\n'.format('ID', 'Ho va ten', 'Noi sinh'))

'''
bai` 11
>>> s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
>>> s
'Neu Mot Ngay Nao Do'
'''
s= 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
d= s[12:-7].title()
e= s.lower().strip('a').lstrip('oa').title()
print(d)
print(e)

'''
bài 12
s = 'aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
Hãy lấy mật mã trong chuỗi s, biết mật mã nằm giữa && và %%. Cố gắng tối thiểu dòng code
'''
s= 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
d= s[12:-7].title()
print(d)

s = 'aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
'''
a= s.find('&&')
b= s.find('%%')
print(a)
print(b)
c= s[33+2:38]
print(c)
'''
'''
a= (s[s.find('&&')+2:s.find('%%')])
print(a)
'''
a= s.split('&&')[-1].split('%%')[0]
print(a)