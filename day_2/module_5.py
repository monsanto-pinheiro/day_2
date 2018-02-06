'''
Created on Feb 6, 2018

@author: mmp
'''
import sys, utils

def sum_all(valor1, valor2):
	
	soma = 0
	for i in range(valor1, valor2):
		soma += i
	if (valor1 <= valor2): soma += valor2
	return soma

if __name__ == '__main__':
	
	if (len(sys.argv) != 3):
		print('usage: module.py <int1> <int2>')
		sys.exit(0)
	
	print(sys.argv)
	valor1 = utils.is_number(sys.argv[1])
	valor2 = utils.is_number(sys.argv[2])
	if (valor1 == None or valor2 == None):
		print('usage: module.py <int1> <int2>')
		sys.exit(0)
	
	print(sum_all(valor1, valor2))
	
	