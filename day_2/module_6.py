'''
Created on Feb 6, 2018

@author: mmp
'''

def fibonacci(value):
	
	if (value < 2): return 1
	for i in range(0, value):
		if (i == 0):
			value_1 = 1
			print(1)
		elif (i == 1):
			value_2 = 1
			print(1)
		else:
			print(value_1 + value_2)
			temp = value_1
			value_1 = value_2
			value_2 = temp + value_2
		

if __name__ == '__main__':
	
	fibonacci(10)