data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，總共有{}筆資料'.format(len(data)))

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為{}'.format(sum_len/len(data)))


#------留言篩選-------
new=[]
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有{}筆留言長度小於100'.format(len(new)))
print(new[0])


good = [d for d in data if 'good' in d]

# for d in data:
# 	if 'good' in d:
# 		good.append(d)
print('一共有{}筆留言提到good'.format(len(good)))
# print(data[0])


#文字計數

wc = {} #word_count
for d in data:
	words = d.split()
	#print(words)
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 #新增新的ＫＥＹ進wc字典


for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
	
while True:
	find = input('請輸入單字')
	if find == 'q':
		break
	elif find in wc:
		print('{}出現的次數為{}次'.format(find, wc[find]))
	else:
		print('這個字沒有出現過喔！')
print('感謝您使用本查詢功能')






