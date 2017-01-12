import re
file = open('regex_sum_342237.txt')
num = list()
for line in file:
	sum = re.findall('[0-9]+',line)
	num = num + sum
total = 0
for n in num:
	total = total + int(n)
print total
