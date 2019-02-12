import csv
import numpy

def open_with_csv(filename, d="\t"):
    data = []
    with open(filename, encoding="utf-8") as tsvin:
        tie_reader = csv.reader(tsvin, delimiter = "\t")
        for line in tie_reader:
            data.append(line)
    return data


data_from_csv = open_with_csv('data.csv')

#for x in data_from_csv:
#    print(x)

FIELDNAMES = ['', 'id', 'priceLabel', 'name', 'brandId', 'brandName', 'imageLink', 'desc', 'vendor', 'patterned', 'material']

DATATYPES = [('myint', 'i'), ('myid', 'i'), ('price', 'f8'), ('name', 'a200'), ('brandId', '<i8'), ('brandName', 'a200'), ('imageUrl', '|S500'), ('description', '|S900'), ('vendor', '|S100'), ('pattern', '|S50'), ('material', '|S50'), ]


def load_data(filename, d="\t"):
    my_csv = numpy.genfromtxt(filename, delimiter=d, skip_header=1, invalid_raise=False, names=FIELDNAMES, dtype=DATATYPES)
    return my_csv


my_csv = load_data("data.csv")

#print(my_csv)

def number_of_records(data_sample):
    return len(data_sample)

number_of_ties = number_of_records(data_from_csv)

#print(number_of_ties - 1)

def number_of_records2(data_sample):
    return data_sample.size


number_of_ties_my_csv = number_of_records2(my_csv)

#print(number_of_ties_my_csv, "ties in our data sample")


def calculate_sum(data_sample):
    total = 0
    for row in data_sample[1:]:
        price = float(row[2])
        total += price
    return total

# print(calculate_sum(data_from_csv))


def calculate_sum_list_comprehension(data_sample):
    prices = [float(row[2]) for row in data_sample[1:]]
    return sum(prices)

# print(calculate_sum_list_comprehension
# (data_from_csv))


def calculate_sum_list_lamda(data_sample):
    prices = list(map(lambda x: float(x[2]), data_sample[1:]))
    return sum(prices)


# print(calculate_sum_list_lamda(data_from_csv))


def calc_numpy_sum(price):
    prices_in_float = [float(line) for line in price]
    total = numpy.sum(prices_in_float)
    return total


price = my_csv['priceLabel']
my_sum = calc_numpy_sum(price)
# print(my_sum)

def find_average(data_sample, header=False):
    if header:
        data_sample = data_sample[1:]
    total = calculate_sum(data_sample)
    size = number_of_records(data_sample)
    average = total / size
    return average


average_price = find_average(data_from_csv, True)
# print("Average = ", average_price)
# print('{:03.2f}'.format(average_price))

midpoint = int(number_of_ties / 2)
message = "The average {} half is ${:03.2f} and contains {} values."
# print(message.format("first", find_average(data_from_csv[:midpoint], True), midpoint))
# print(message.format("second", find_average(data_from_csv[midpoint:], False), midpoint))

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


# print(find_max(data_from_csv[1:], 2))
# print(find_min(data_from_csv[1:], 2))
# print(find_max_min(data_from_csv[1:], 2, "max"))
# print(find_max_min(data_from_csv[1:], 2, "min"))


price = my_csv['priceLabel']
price_in_float = [float(x) for x in price]
numpy_max = numpy.amax(price_in_float)
numpy_min = numpy.amin(price_in_float)
# print(numpy_max)
# print(numpy_min)

