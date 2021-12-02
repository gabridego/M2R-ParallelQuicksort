import os
import sys
import subprocess
import time
import math
import random
from pathlib import Path
from decimal import Decimal

from datetime import datetime

import cpuinfo


def run(start, end, step, reps=20):
    output_dir = f'data/{os.uname()[1]}_{datetime.today().strftime("%Y-%m-%d")}'
    os.makedirs(output_dir, exist_ok=True)
    output_file = f'{output_dir}/measurements_{datetime.now().strftime("%H_%M")}'
    output_file_text = f'{output_file}.txt'
    output_file_csv = f'{output_file}.csv'

    Path(output_file_text).touch()

    items = list(range(start, end, step))
    items.append(end)
    items = items * reps
    random.shuffle(items)
    num_len = len(items)

    for i, item in enumerate(items):
        print(f'[{i+1}/{num_len}]: {"{:.2E}".format(Decimal(item))}')
        with open(output_file_text, 'a') as file:
            file.write(f'Size: {item}\n')
        subprocess.run(f"./src/parallelQuicksort {item} >> {output_file_text}", shell=True)

    cpuinfos = cpuinfo.get_cpu_info()
    os.setxattr(output_file_text, 'user.cpu', f'{cpuinfos["brand_raw"]}'.encode())
    os.setxattr(output_file_text, 'user.cores', f'{os.cpu_count()}'.encode())
    os.setxattr(output_file_text, 'user.ram', f'{os.sysconf("SC_PAGE_SIZE") * os.sysconf("SC_PHYS_PAGES") / (1024.**3)}'.encode())
    os.setxattr(output_file_text, 'user.start', f'{start}'.encode())
    os.setxattr(output_file_text, 'user.end', f'{end}'.encode())
    os.setxattr(output_file_text, 'user.step', f'{step}'.encode())
    os.setxattr(output_file_text, 'user.reps', f'{reps}'.encode())

    subprocess.run(f"perl scripts/csv_quicksort_extractor.pl < {output_file_text} > {output_file_csv}", shell=True)

if __name__ == '__main__':
    argslen = len(sys.argv)
    if argslen < 4:
        print("Error: Please provide start, end and step arguments")
        sys.exit()

    start = int(float(sys.argv[1]))
    end = int(float(sys.argv[2]))
    step = int(float(sys.argv[3]))
    reps = 20

    if argslen == 5:
        reps = int(float(sys.argv[4]))

    run(start, end, step, reps)
