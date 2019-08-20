#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    count = 0
    for i in range(len(s)):
        if s[i] == "D":
            count -= 1
        elif s[i] == "U":
            count += 1
            if count == 0:
                valleys += 1
    return valleys

