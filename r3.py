
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:   #字串可當成清單來看待
	s = line.split(' ') 
	time = s[0][:5]
	name = s[0][5:]    
	print(time,name)