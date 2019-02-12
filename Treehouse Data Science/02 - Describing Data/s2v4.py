from s2v3 import *

def find_average(data_sample, header=False):
    if header:
        data_sample = data_sample[1:]
    total = calculate_sum(data_sample)
    size = number_of_records(data_sample)
    average = total / size
    return average


average_price = find_average(data_from_csv, True)
print("Average = ", average_price)
print('{:03.2f}'.format(average_price))

midpoint = int(number_of_ties / 2)
message = "The average {} half is ${:03.2f} and contains {} values."
print(message.format("first", find_average(data_from_csv[:midpoint], True), midpoint))
print(message.format("second", find_average(data_from_csv[midpoint:], False), midpoint))
