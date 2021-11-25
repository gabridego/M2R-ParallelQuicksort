import sys
import os
import subprocess
import random
from datetime import date, datetime

output_directory = os.path.join("data", os.uname()[1] + '_' + date.today().strftime("%Y-%m-%d"))
os.makedirs(output_directory, exist_ok=True)
output_file = os.path.join(output_directory, "measurements_" + datetime.now().strftime("%H_%M") + ".txt")
output_csv = os.path.splitext(output_file)[0] + ".csv"

sizes = []
for size in [100, 1000, 10000, 100000, 200000, 400000, 600000, 800000, 1000000]:
	sizes.extend([str(size)] * 20)
random.shuffle(sizes)

with open(output_file, 'w') as f:
	while len(sizes) != 0:
		size = sizes.pop()
		subprocess.run(["echo", f"Size: {size}"], stdout=f)
		subprocess.run(["./src/parallelQuicksort", size], stdout=f)

with open(output_file, 'r') as fin:
	with open(output_csv, 'w') as fout:
		subprocess.run(["perl", "scripts/csv_quicksort_extractor.pl"], stdin=fin, stdout=fout)
