a= "Nhan Tran 12a2"
b= a.split('n')
#b= a.split(' ', 3)
print(a)
print(b)
c= a.rsplit('n',1)
print(c)
d= a.rpartition('an ')
#d= a.lpartition(' ')
print(d)
e= a.count('n')
#count('',start,end)
f= a.count('n',1,8)
print(e)
print(f)
mgaaa= "abcdefg"
#g= mgaaa.startswith(mgaaa)
g= mgaaa.startswith('a',1,0)
#g= mgaaa.endswith(mgaaa)
print(g)
nhan= a.find('21')
Nhan= a.index('12')
#index se~ ra loi~ neu khong tim thay.
print(nhan)
print(Nhan)
'''str.rfind(sub[, start[, end]])
Return the highest index in the string where substring sub is found, 
such that sub is contained within s[start:end]. 
Optional arguments start and end are interpreted as in slice notation. Return -1 on failure.'''
nn= a.islower()
#nn= a.isupper()
print(nn)
mm=a.isdigit()
print(mm)
#mm=a.isspace()