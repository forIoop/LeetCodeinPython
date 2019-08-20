#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    jumps, i = 0, 0
    while i < len(c)-1:
        # if 2 cloud jumps
        if i+2 < len(c) and c[i+2] != 1:
            i += 1
        jumps += 1
        i += 1
    return jumps
