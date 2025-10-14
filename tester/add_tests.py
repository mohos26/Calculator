from math import *
from math import factorial as fac


with open("test.txt") as file_in, open("test.csv", "a") as file_out:
	while True:
		line = file_in.readline().strip()
		if not line:
			break
		if '=' in line:
			line = line.split('=')
			line[0] = line[0].replace("^", "**")
			file_out.write(line[0].replace(' ', '') + ',' + line[1] + '\n')
		else:
			file_out.write(line.replace(' ', '') + ',' + str(round(eval(line.replace(' ', '')), 6)) + '\n')
