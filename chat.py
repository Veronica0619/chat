
def read_file(filename):
	lines =[]
	with open (filename , 'r',encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())#去掉字串附屬的功能再存進Line
	return lines

def convert(lines):
	new = []
	person = None #person = '123'
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom': #另外如果
			person = 'Tom'
			continue
		if person: #if person != '123':
			new.append(person + ': ' + line)
	return new	

def write_file(filename,lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')



def main():
	lines = read_file('input.txt') 
	lines = convert(lines)
	write_file('output.txt',lines)
	# print(lines)

main() 
#使用呼叫的動作#進入點