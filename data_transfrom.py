# -*- coding: utf-8 -*-

import numpy as np 

# 口令中出现的字母表
# alphabetas = [
# 	# 数字
# 	'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 
# 	# 字母
# 	'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 
# 	'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 
# 	'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
# 	'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 
# 	# 特殊字符
# 	',', '.', '/', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', 
# 	')', '_', '+', '<', '>', '?', ' ', '{', '}', '|', ':', '\"', '[', 
# 	']', '\\', '\'', ';', '`', '-', '='
# ]
alphabetas = []
def generate_alphabetas():
	with open('../data/rockyou_small.txt', 'r') as f:
		orginal_password = f.readlines()
		text = ''.join(orginal_password)
		global alphabetas
		alphabetas = sorted(list(set(text)))
		alphabetas.insert(0, '□')

def char_to_vector(c, start=False, end=False):
	"""
		convert character to 1-of-N code
	"""
	#词汇表大小，加上一个起始符，以换行符作为结束符
	vec_len = len(alphabetas)
	vector = [ 0 for _ in range(vec_len) ]

	vector[alphabetas.index(c)] = 1
	return vector

def password_to_vector(password, width ):

	X = []
	Y = []

	if len(password) - width > 0:
		for i in range(len(password)-width):
			x = [ char_to_vector(c) for c in password[i:i+width] ]
			y = char_to_vector(password[i+width]) 
			X.append(x)
			Y.append(y)
	else:
		x = [char_to_vector(c) for c in password]		
		y = [0 for _ in range(len(alphabetas))]
		for i in range(width - len(password)):			
			vec_zero = [0 for _ in range(len(alphabetas))]
			x.append(vec_zero)
		X.append(x)
		Y.append(y)

	return X, Y


def vector_to_char(vec):
	# 结尾字符
	if vec[-1] == 1:
		return '\n'
	# 开始字符
	if vec[0] == 1:
		return '□'

	for i, e in enumerate(vec):
		if e == 1:
			return alphabetas[i-1]


def transform_dataset(seq_len):
	print(alphabetas)
	with open('../data/rockyou_small.txt', 'r') as f:
		X = []
		Y = []

		for i, pw in enumerate(f):
			pw_list = list(pw)
			pw_list.insert(0,'□')
			pw = "".join(pw_list)
			x, y = password_to_vector(pw.rstrip(),width=seq_len)
			print(i)
			X += x
			Y += y
		#print(X[0])
		#print(X[1])
		#print(X[2])
		''' 
		for item in X:
			print(np.array(item).shape)
		'''
		X = np.array(X)
		Y = np.array(Y)
		print(X.shape, Y.shape)
		np.savez('../data/dataset_%d'%seq_len, X=X, Y=Y)


def main():	
	generate_alphabetas()
	transform_dataset(seq_len=10)
		

if __name__ == '__main__':	
	main()


