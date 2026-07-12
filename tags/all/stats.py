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
	with open('families.csv', encoding='utf-8') as f:
		reader = csv.DictReader(f, fieldnames=["Family", "Axes", "Group/Tag", "Weight", "Providence"])
		records = [r for r in reader]

	count_by_family = collections.defaultdict(int)
	human_count = 0
	predicted_count = 0
	for r in records:
		count_by_family[r["Family"]] += 1
		if r.get("Providence") == "predicted":
			predicted_count += 1
		else:
			human_count += 1
	
	counts = sorted(count_by_family.values())

	print("Num tags", len(records))
	if predicted_count > 0:
		print(f"  Human tags: {human_count}")
		print(f"  Predicted tags: {predicted_count}")
	print("Mean tags ", mean(counts))
	print("Median tags", median(counts))
	print("Stdev tags", stdev(counts))
	print("Max tags", max(counts))


if __name__ == '__main__':
	main()