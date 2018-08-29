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

new=[]


for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有{}筆留言長度小於100'.format(len(new)))
print(new[0])


good = []

for d in data:
	if 'good' in d:
		good.append(d)
print('一共有{}筆留言提到good'.format(len(good)))