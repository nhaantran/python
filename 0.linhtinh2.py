#indexing và cắt chuỗi (từ 0 đến n-1)*lưu ý nhen!
A = "abc def"
B = A[1:6]
C = A[-2]
print(B)

'''
bai` 11
>>> s = 'aaaAAaaaooaaneu mot Ngay naO Doaaaaaaa'
>>> s
'Neu Mot Ngay Nao Do'
'''

s = 'aaaaaaaAAAAAaaa//123123//000000//&&TTT%%abcxyznontqfadf'
#code = s.split('&&')[-1].split('%%')[0]
#code = s.split('&&')[-1]
code= s.split('%%')
print(code)

lst = [[1, 2], ['abc', 'def']]
lst.sort()
print(lst)
