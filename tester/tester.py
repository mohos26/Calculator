import sys
sys.path.append("..")
from evaluate_postfix import evaluate_postfix
from infix_to_postfix import infix_to_postfix
from parsing import parsing
from math import *
import csv


with open("test.csv") as file:
	csv_reader = csv.reader(file)

	header = next(csv_reader)

	i = 1
	for eq, value in csv_reader:
		# debug
		# print(eq, value)
		output = evaluate_postfix(infix_to_postfix(parsing(eq)))
		if float(value) != round(float(output), 6):
			print(f"Test [{i}]: {eq}")
			print(f"Found: {output}; Expect: {value}")
			exit(1)
		i += 1

print("!!! All Tests Are Passed !!!")
