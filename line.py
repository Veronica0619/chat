
def read_file(filename):
	lines =[]
	with open (filename , 'r',encoding = 'utf-8-sig') as f: #-sig 去掉怪怪符號
		for line in f:
			lines.append(line.strip())#去掉字串附屬的功能再存進Line
	return lines

def convert(lines):
	person = None #person = '123'
	allen_word_count = 0          # 前3個 n[:3]
	viki_word_count = 0 
	allen_sticker_count = 0 
	viki_sticker_count = 0 
	allen_image_count = 0
	viki_image_count = 0         # 中間 n[2:4]
	for line in lines:            # 結尾 n[-2:] n[2:]
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count = allen_sticker_count + 1
			elif s[2] == '圖片':
				allen_image_count = allen_image_count + 1
			else:
				for m in s[2:]:
					allen_word_count = len(m) + allen_word_count
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count = viki_sticker_count + 1
			elif s[2] == '圖片':
				viki_image_count = viki_image_count + 1
			else:
				for m in s[2:]:
					viki_word_count = len(m) + viki_word_count

	print('Allen 說了', allen_word_count ,'幾個字，傳了',allen_sticker_count, '個貼圖，以及',allen_image_count,'圖片')
	print('Viki 說了', viki_word_count ,'幾個字，傳了',viki_sticker_count, '個貼圖，以及',viki_image_count,'圖片')

	
	

def write_file(filename,lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')



def main():
	lines = read_file('LINE-Viki.txt') 
	lines = convert(lines)
	# write_file('output.txt',lines)
	# print(lines)

main() 
#使用呼叫的動作#進入點