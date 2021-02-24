from math import *
from prettytable import PrettyTable

x = PrettyTable()

print('ax² + bx + c = 0')

def square(a, b, c):
	x.field_names = ['x1', 'x2']
	D = pow(b, 2) - 4 * a * c
	x1 = 1
	x2 = 1

	if D < 0:
		x.add_row(['-', '-'])
		print(x)
	elif D == 0:
		x1 = round(-b / (2 * a), 5)
		x.add_row([f'{x1}...', '-'])
		print(x)
	elif D > 0:
		x1 = round((-b + sqrt(D)) / (2 * a), 5)
		x2 = round((-b - sqrt(D)) / (2 * a), 5)
		x.add_row([f'{x1}...', f'{x2}...'])
		print(x)

one, two, three = float(input('Введите a: ')), float(input('Введите b: ')), float(input('Введите c: '))

square(one, two, three)