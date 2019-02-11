from s2v2 import *

def calculate_sum(data_sample):
    total = 0
    for row in data_sample[1:]:
        price = float(row[2])
        total += price
    return total

#print(calculate_sum(data_from_csv))


def calculate_sum_list_comprehension(data_sample):
    prices = [float(row[2]) for row in data_sample[1:]]
    return sum(prices)

print(calculate_sum_list_comprehension(data_from_csv))