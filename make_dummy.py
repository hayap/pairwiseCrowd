# -*- coding: utf-8 -*-
import random

path = './dummy_sushi/sushi3a.5000.10.order'
dataset = []
#sample number
SUSHI_NUM = 10
WORKER_NUM = 20
SAMPLE_NUM = 30

# read dataset
with open(path) as f:
	l = f.readlines()
l = l[1:WORKER_NUM+1]
s = -1

# create random pair
for l_line in l:
	s = s+1
	order = l_line.strip().split(' ')[2:]
	taple_list = [] 
	for num in range(SAMPLE_NUM):
		fin_gen = False
		while (not fin_gen):
			a = random.randint(0,SUSHI_NUM-2)
			b = random.randint(a+1,SUSHI_NUM-1)
			t = (s,order[a],order[b])
			if not t in taple_list:
				taple_list.append(t)
				fin_gen = True
	dataset.extend(taple_list)

# write file
path_w = './dummy_sushi/sushi3a.pairwise'
path_w = path_w + '.' + str(WORKER_NUM) + '.' + str(SAMPLE_NUM)
with open(path_w,mode='w') as f:
	f.write(str(SUSHI_NUM) + ' ' + str(WORKER_NUM) + ' ' + str(SAMPLE_NUM) + '\n')
	for t in dataset:
		f.write(str(t[0])+ ' ' + str(t[1]) + ' ' + str(t[2]) + '\n')

