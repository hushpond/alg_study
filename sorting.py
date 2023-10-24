import random
n = 50000
random_numbers = list(range(1, n + 1))
random.shuffle(random_numbers)

import time 
import math
start = time.time()
math.factorial(10000)

def sorting(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return sorting(lesser_arr) + equal_arr + sorting(greater_arr)

sorting(random_numbers)

for num in random_numbers:
    print(num)
    
end = time.time()
print(f"{end - start:.5f} sec")
