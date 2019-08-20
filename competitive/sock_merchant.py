#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ht = dict()
    pairs = 0

    for i in range(len(ar)):
        ht[ar[i]] = ht.get(ar[i],0) + 1
    
    for value in ht.values():
            pairs += value // 2
    return pairs



    return ht
