my_apple_bin = ['green', 'red', 'yellow', 'green', 'green', 'red', 'yellow']
your_apple_bin = ['green', 'red', 'red', 'green', 'yellow', 'yellow', 'yellow']

my_green_apples = my_apple_bin.count('green')
your_green_apples = your_apple_bin.count('green')

total_green_apples = my_green_apples + your_green_apples


print("I have " + str(my_green_apples) + " green apples.")
print("You have " + str(your_green_apples) + " green apples.")
print("There are " + str(total_green_apples) + " green apples total.")