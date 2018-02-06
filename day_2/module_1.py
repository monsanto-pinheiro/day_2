'''
Created on Feb 6, 2018

@author: mmp
'''


def is_number(valor):
	
	try:
		return int(valor)
	except:
		return None


if __name__ == '__main__':
	
	while True:
		valor_1 = input('first number integer? ')
		valor_1 = is_number(valor_1)
		if (valor_1 != None): break
		
	while True:
		valor_2 = input('second number integer? ')
		valor_2 = is_number(valor_2)
		if (valor_2 != None): break
	
	if (valor_1 == valor_2): print('IGUAIS')
	elif (valor_1 > valor_2): print('Maior: {}'.format(valor_1))
	else: print('Maior: {}'.format(valor_2))
	