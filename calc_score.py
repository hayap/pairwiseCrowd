# -*- coding: utf-8 -*-

import math
import numpy as np
from scipy.optimize import minimize

dataset = []
sushi_num = 0
worker_num = 0
sample_num = 0
data_path = './dummy_sushi/sushi3a.pairwise.20.30'

LAMBDA = 0.1
s = []
eta = []

def read_data():
	tmp = []
	with open(data_path) as f:
		lines = f.readlines()
	header = lines[0].strip()
	lines = lines[1:]

	global sushi_num
	global worker_num
	global sample_num
	sushi_num,worker_num,sample_num = header.split(' ')
	sushi_num = int(sushi_num)
	worker_num = int(worker_num)
	sample_num = int(sample_num)

	for l in lines:
		d = l.strip().split(' ')
		d = [int(n) for n in d]
		tmp.append(d)
	global dataset
	dataset = tmp

def L(eta,s):
	obj = 0
	for d in dataset:
		bunbo = math.exp(s[d[1]]) + math.exp(s[d[2]])
		try:
			obj = obj + math.log( eta[d[0]] * math.exp(s[d[1]]) / bunbo + (1 - eta[d[0]]) * math.exp(s[d[2]]) / bunbo)
		except:
			print(eta[d[0]])
			print(s[d[1]])
			print(s[d[2]])
	return obj

def R(s):
	obj = 0
	for i in range(sushi_num):
		obj = obj + math.log(math.exp(s[sushi_num]/(math.exp(s[sushi_num]) + math.exp(s[i]))))\
		          + math.log(math.exp(s[i]/(math.exp(s[sushi_num]) + math.exp(s[i]))))
	return obj

def obj_func1(eta):
	return - L(eta,s) - LAMBDA * R(s)

def obj_func2(s):
	return - L(eta,s) - LAMBDA * R(s)

def init_params():
	global s
	s = [0.5 for i in range(int(sushi_num)+1)]
	global eta
	eta = [1 for i in range(worker_num)]

if __name__=='__main__':
	read_data()
	init_params()
	
	for i in range(20):
		result = minimize(obj_func2, x0=s, method='L-BFGS-B')
		s = result.x
		print(s)

		bounds_eta = [(0,1) for i in range(worker_num)]
		result = minimize(obj_func1, x0=eta, bounds=bounds_eta,method='L-BFGS-B')
		eta = result.x
		print(eta)

	s = s[0:sushi_num]
	b = np.argsort(s)
	b = b[-1::-1]
	print(b)
