set= {5, 8, 1, 9, 4}
sum = 0
for value in set:
	sum+=value
print(sum)

print('---------------------------')
lst= [[1,2,3],[4,5,6]]
for value in lst:
	value = list(list(lst))
	value[0][0]= 'None'
	value[1][0]= 'None'
print(lst)
print('----------------------')
lst = [[1.2,3],[4,5,6]]
for i in lst:
	i[0]= 'None'
print(lst)