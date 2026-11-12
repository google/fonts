"""
Lists families with fewer than the median # tags.

Pass a # to cutoff at <= that # of tags. By default lists items
with < median #tags.

Usage:

	# One-time: setup a venv

	$ python3 -m venv venv
	$ source venv/bin/activate
	$ pip install requests

	# Once you have a venv

	# list families with < median tags
	$ python3 lowtags.py
	# list families with 0 tags
	$ python3 lowtags.py 0
"""

import collections
import csv
from pathlib import Path
import requests
from statistics import mean, median, stdev
import sys

def main():
	args = sys.argv[1:]
	if len(args) > 1:
		sys.exit("Too many args")

	with open('families.csv') as f:
		reader = csv.DictReader(f)
		records = [r for r in reader]

	count_by_family = collections.defaultdict(int)
	tags_by_family = collections.defaultdict(list)

	# we want a result for every public family, even if it's 0 tags
	resp = requests.get("https://fonts.google.com/metadata/fonts")
	resp.raise_for_status()
	for family in resp.json()["familyMetadataList"]:
		count_by_family[family["family"]] = 0

	for r in records:
		count_by_family[r["Family"]] += 1
		tags_by_family[r["Family"]].append(r["Group/Tag"])
	counts = sorted(count_by_family.values())

	if len(args) == 1:
		cutoff = int(args[0])
	else:
		cutoff = median(counts) - 1

	for (family, count) in sorted(count_by_family.items()):
		if count > cutoff:
			continue
		print(family, count, sorted(tags_by_family[family]))


if __name__ == '__main__':
	main()