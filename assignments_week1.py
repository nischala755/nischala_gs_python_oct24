''' Check if a year is a leap year or not'''
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year = 2024
print(f"{year} is a leap year: {is_leap_year(year)}")  # Output: True

''' Check if a given number is compoistie or not'''
def is_composite_number(n):
    if n < 4:
        return False  # 0, 1, 2, 3 are not composite numbers
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

# Example usage:
digit = 9
print(f"{digit} is a composite number: {is_composite_number(digit)}")  # Output: True

''' Check if character is alphanumeric or not'''
def is_alphanumeric(char):
    return char.isalnum()

# Example usage:
character = 'A1'
print(f"'{character}' is alphanumeric: {is_alphanumeric(character)}")  # Output: True

character = '@'
print(f"'{character}' is alphanumeric: {is_alphanumeric(character)}")  # Output: False

''' Accept a number and find sum of digits'''
def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Example usage:
num = 12345
print(f"Sum of digits in {num}: {sum_of_digits(num)}")  # Output: 15

''' Accept a Number and Count the Number of Digits'''
def count_digits(number):
    return len(str(number))

# Example usage:
num = 12345
print(f"Number of digits in {num}: {count_digits(num)}")  # Output: 5

''' Accept a Number and Find Biggest/Smallest Digit'''
def biggest_smallest_digit(number):
    digits = [int(digit) for digit in str(number)]
    return max(digits), min(digits)

# Example usage:
num = 12345
biggest, smallest = biggest_smallest_digit(num)
print(f"Biggest digit: {biggest}, Smallest digit: {smallest}")  # Output: 5, 1

'''Find Sum of Even/Odd Digits in the Number'''

def sum_even_odd_digits(number):
    even_sum = sum(int(digit) for digit in str(number) if int(digit) % 2 == 0)
    odd_sum = sum(int(digit) for digit in str(number) if int(digit) % 2 != 0)
    return even_sum, odd_sum

# Example usage:
num = 12345
even_sum, odd_sum = sum_even_odd_digits(num)
print(f"Sum of even digits: {even_sum}, Sum of odd digits: {odd_sum}")  # Output: 6, 9

'''Find the Frequency of a Digit in the Number'''
def digit_frequency(number, digit):
    return str(number).count(str(digit))

# Example usage:
num = 123453
digit = 3
print(f"Frequency of {digit} in {num}: {digit_frequency(num, digit)}")  # Output: 1

'''  Find Sum of Odd Placed Even Digits in the Number'''
def sum_odd_placed_even_digits(number):
    return sum(int(digit) for index, digit in enumerate(str(number)) if (index % 2 == 0) and (int(digit) % 2 == 0))

# Example usage:
num = 246813
print(f"Sum of odd placed even digits in {num}: {sum_odd_placed_even_digits(num)}")  # Output: 8 (2 + 6)

'''  Find the 2nd Smallest Digit in the Number'''
def second_smallest_digit(number):
    digits = sorted(set(int(digit) for digit in str(number)))
    return digits[1] if len(digits) > 1 else None  # Return None if there's no second smallest

# Example usage:
num = 123456
print(f"2nd smallest digit in {num}: {second_smallest_digit(num)}")  # Output: 2


'''Accept a string and access all the characters one by one'''
my_string = input('Enter a place name: ')

print(f'Type of {my_string} is {type(my_string)}')

for character in my_string: # for each loop
    print(f'{character}, Type={type(character)}')

first_character = chr(my_string[0])
print(f'first charatcer = {first_character}, Type = {type(character)}')


my_string = input('Enter a place name: ') # mumbai

my_string = my_string.upper()
print(f'my_string = {my_string}')
#print(f'string1 = {string1}')

# print(f'String in Upper case = {my_string.upper()}')

number1 = 15
number2 = 25.5

print(f'type of number1 = {type(number1)}')
print(f'type of number2 = {type(number2)}')

print(number1.bit_count)
print(number1.__sizeof__())
print(number1.__eq__(15))

# 26. Find sum of the series: n + n² + n³ + ... up to 10 terms
def sum_of_series_n(n):
    return sum(n**i for i in range(1, 11))

# Example usage:
n = 2
print(f"Sum of the series for n={n}: {sum_of_series_n(n)}")  # Output: 2046


# 27. Find sum of the series: 1 - n + n² - n³ + ... up to M terms
def sum_of_alternating_series(n, m):
    return sum((-1)**i * n**i for i in range(m))

# Example usage:
n = 2
m = 5
print(f"Sum of the series for n={n} and m={m}: {sum_of_alternating_series(n, m)}")  # Output: 1


# 28. Find sum of the series: 1 - n/3 + n²/5 - n³/7 + n⁴/9 ...
# (1 < n < 5 and 1 < m < 10)
def sum_of_custom_series(n, m):
    return sum((-1)**i * (n**i) / (2*i + 1) for i in range(m))

# Example usage:
n = 3
m = 5
print(f"Sum of the series for n={n} and m={m}: {sum_of_custom_series(n, m)}")  # Output: 1.52


# 29. Print the Nth Prime number
def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1
    return num

# Example usage:
n = 10
print(f"The {n}th prime number is: {nth_prime(n)}")  # Output: 29


# 30. Check if the sum of Prime digits in a number is a Prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_prime_digits(number):
    prime_digits = [int(d) for d in str(number) if d in '2357']
    digit_sum = sum(prime_digits)
    return digit_sum, is_prime(digit_sum)

# Example usage:
number = 1234567
digit_sum, is_digit_sum_prime = sum_of_prime_digits(number)
print(f"Sum of prime digits in {number}: {digit_sum}, Is it prime? {is_digit_sum_prime}")  # Output: (Sum, True/False)


# 31. Print Nth term of the following series: 1, 2, 2, 3, 3, 5, 5, 7, 8, 11, 13, 13
def nth_term_series(n):
    series = []
    a, b = 1, 2
    for _ in range(n):
        if len(series) < 2 or series[-1] != b:
            series.append(b)
        a, b = b, a + b if len(series) % 2 == 0 else a + 1
    return series[n - 1]

# Example usage:
n = 10
print(f"The {n}th term of the series is: {nth_term_series(n)}")  # Output: 11

