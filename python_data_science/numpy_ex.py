#! /usr/bin/env python3

import numpy as np
import csv
import sys

# print(np.array([1, 4, 2, 5, 3]))
#
# print(np.array([range(i, i + 3) for i in [2, 4, 6]]))

with open(sys.argv[1], 'rt') as csv_file:
    games_data = csv.reader(csv_file)
    for row in games_data:
        print(row)
