# Exercise 1

def calculate_area_triangle(base , height):
    area = 0

    area = (base * height) / 2

    return area

print('Exercise 1:', calculate_area_triangle(10, 5))

# Exercise 2

def simple_interest(principal , rate , time):
    interest = 0

    interest = (principal * rate * time) / 100

    return interest

print('Exercise 2:', simple_interest(1000, 5, 2))

# Exercise 3

def apply_discount(price, discount):
    price_after_discount = 0

    price_after_discount = price * ((100 - discount)/100)

    return price_after_discount

print('Exercise 3:', apply_discount(100, 25))

# Exercise 4 

def convert_temperature(temperature , unit):
    temp = 0

    if unit == 'C':
        temp = (temperature * 9/5) + 32
    elif unit == 'F':
        temp = (temperature - 32) * 5/9
    else:
        print('you can not convert this')

    return temp

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# Exercise 5

def sum_to(num):
    sum = num

    for num in range(num):
        sum += num

    return sum

print('Exercise 5:', sum_to(6))

# Exercise 6 

def largest(num1 , num2 , num3):
    largest = 0

    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    return largest

print('Exercise 6:', largest(10, 4, 2))

# Exercise 7 

def calculate_tip(bill , tip_percentage):
    tip = 0

    tip = bill * ((tip_percentage)/100)

    return tip

print('Exercise 7:', calculate_tip(50, 20))

# Exercise 8

def product(*args):
    product = 1

    for num in args:
        product *=num

    return product

print('Exercise 8:', product(2, 5, 5))

# Exercise 9 

def basicCalculator(num1 , num2 , operation):
    result = 0

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    else:
        result = num1 / num2


    return result

print('Exercise 9 Result:', basicCalculator(10, 5, 'divide'))