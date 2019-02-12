from s2v4 import *


def find_max(data_sample, col):
    price_list = [float(row[col]) for row in data_sample]
    return max(price_list)


def find_min(data_sample, col):
    price_list = [float(row[col]) for row in data_sample]
    return min(price_list)


def find_max_min(data_sample, col, m):
    price_list = [float(row[col]) for row in data_sample]
    if str(m).strip() == "max":
        return max(price_list)
    elif str(m).strip() == "min":
        return min(price_list)
    else:
        raise ValueError('Please input "Max" or "Min" for the 3rd function argument')


print(find_max(data_from_csv[1:], 2))
print(find_min(data_from_csv[1:], 2))
print(find_max_min(data_from_csv[1:], 2, "max"))
print(find_max_min(data_from_csv[1:], 2, "min"))