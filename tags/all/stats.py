"""
Gives basic stats about tags.

Usage:

	$ python3 stats.py
	Num tags 9125
	Mean tags  5.086399108138239
	Median tags 5.0
	Stdev tags 2.474364733745681
	Max tags 27
"""

import collections
import csv
from pathlib import Path
from statistics import mean, median, stdev

def main():
	with open('families.csv') as f:
		reader = csv.DictReader(f)
		records = [r for r in reader]

	count_by_family = collections.defaultdict(int)
	for r in records:
		count_by_family[r["Family"]] += 1
	
	counts = sorted(count_by_family.values())

	print("Num tags", len(records))
	print("Mean tags ", mean(counts))
	print("Median tags", median(counts))
	print("Stdev tags", stdev(counts))
	print("Max tags", max(counts))


if __name__ == '__main__':
	main()