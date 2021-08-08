k= 20
while k-5 >1:
	print('k=',k)
	k -=  5
'''
name = 'Nhân Trần'
start = 0
skt= len(name)
while skt > start:
	print(start,'stands for', name[start])
	start +=1
'''
name = 'NhânTrần'
sốkítự = len(name)
start = 0
while sốkítự > start:
	print(name[start],'là kí tự thứ:',start, 'trong tên tui')
	start +=1

'''
five_even_numbers = []
k_number = 1

while True: # vòng lặp vô hạn vì giá trị này là hằng nên ta không thể tác động được
    if k_number % 2 == 0: # nếu k_number là một số chẵn
        five_even_numbers.append(k_number) # thêm giá trị của k_number vào list
    if len(five_even_numbers) == 5: # nếu list này đủ 5 phần tử
        break # thì kết thúc vòng lặp
    k_number += 1
print(five_even_numbers)
print(k_number)
'''
'''
k = 0
while k <10:
	if k%2 == 0:
		k+=1
		continue
	print(k,'la so le')
	k +=1		
'''
#cách này nhanh hơn
k= 0
while k<10:
	k+=1
	if k%2==0:
		continue
	print(k,'là số lẻ')
	
