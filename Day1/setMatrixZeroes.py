from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    row_set = set()
    col_set = set()
    for i, l in enumerate(matrix):
        for j, ele in enumerate(l):
            if not ele:
                row_set.add(i)
                col_set.add(j)
    for i in row_set:
        for j in range(len(matrix[0])):
            matrix[i][j] = 0
    for j in col_set:
        for i in range(len(matrix)):
            matrix[i][j] = 0