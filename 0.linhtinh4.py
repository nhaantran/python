with open('16.While.txt') as a:
	data= a.readlines()
length = len(data)
idx = 0
new_content = ''
while length > idx:
	line_list= data[idx].split()
	length_line = len(line_list) 
	idx_line = 0
	while length_line > idx_line:
		if line_list[idx_line]== 'Kteam':
			line_list[idx_line -1]= 'How'
		idx_line+=1
	new_content+= ' '.join(line_list) + '\n'
	idx+=1

with open('kteam.txt', 'w') as new_f:
    # ghi nội dung mới vào file kteam.txt
    new_f.write(new_content)