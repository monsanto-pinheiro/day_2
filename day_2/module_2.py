'''
Created on Feb 6, 2018

@author: mmp
'''
import utils

def soma_duas_vezes(valor_1, valor_2):
	valor_1 = utils.is_number(valor_1)
	valor_2 = utils.is_number(valor_2)
	return valor_1 + valor_2 if valor_1 != None and valor_2 != None else None

if __name__ == '__main__':
	
#	print(soma_duas_vezes(10, 20))

	while True:
		valor = input('Introduza um valor inteiro: ')
		valor = utils.is_number(valor)
		if valor != None: break
		
	if ((valor % 2) == 0): print ('even')
	else: print ('odd')
