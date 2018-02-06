'''
Created on Feb 6, 2018

@author: mmp
'''
import utils
import sys

if __name__ == '__main__':
	
	vect_float = []
	while True:
		number = input('float number? ')
		number = utils.is_float(number)
		if (number != None):
			if (number == 0.0): break
			vect_float.append(number)
	
	if (len(vect_float) == 0): 
		print('No values in vector')
		sys.exit(0)
		
	print(vect_float)
	max = None
	min = None
	soma = 0
	for value in vect_float:
		if (max == None or max < value): max = value
		if (min == None or min > value): min = value
		soma += value
		
	print('Max: {}  Min:  {}   Average: {}'.format(max, min, soma/len(vect_float)))

	