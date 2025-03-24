# 1
def evens_and_odds(num):
    evens = 0
    odds = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            evens += 1
        else:
            odds += 1
    return f"The number of evens are {evens}. The number of odds are {odds}."
print(evens_and_odds(100))

# 2
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
print(factorial(5))

# 3
def is_empty(value):
    if value == "" or value is None or (isinstance(value, (list, dict, set)) and len(value) == 0):
        return True
    return False
print(is_empty("")) 
print(is_empty([1, 2, 3])) 


# 4
def calculate_mean(lst):
    return sum(lst) / len(lst) if lst else 0

def calculate_median(lst):
    sorted_lst = sorted(lst)
    n = len(sorted_lst)
    if n % 2 == 0:
        return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
    else:
        return sorted_lst[n // 2]

from collections import Counter
def calculate_mode(lst):
    count = Counter(lst)
    max_count = max(count.values())
    return [item for item, cnt in count.items() if cnt == max_count]

def calculate_range(lst):
    return max(lst) - min(lst) if lst else 0

def calculate_variance(lst):
    mean = calculate_mean(lst)
    return sum((x - mean) ** 2 for x in lst) / len(lst) if lst else 0

import math
def calculate_std(lst):
    return math.sqrt(calculate_variance(lst)) if lst else 0

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Mean: {calculate_mean(data)}") 
print(f"Median: {calculate_median(data)}")  
print(f"Mode: {calculate_mode(data)}")  
print(f"Range: {calculate_range(data)}") 
print(f"Variance: {calculate_variance(data)}") 
print(f"Standard Deviation: {calculate_std(data)}") 

