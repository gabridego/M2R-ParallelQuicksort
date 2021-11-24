import sys
import subprocess
import random

out_file = sys.argv[1]

sizes = []
for size in [100, 1000, 10000, 100000, 200000, 400000, 600000, 800000, 1000000]:
	sizes.extend([str(size)] * 20)
random.shuffle(sizes)

with open(out_file, 'w') as f:
	while len(sizes) != 0:
		size = sizes.pop()
		process = subprocess.run(["echo", f"Size: {size}"], stdout=f)
		process = subprocess.run(["./src/parallelQuicksort", size], stdout=f)
