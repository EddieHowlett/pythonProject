from itertools import filterfalse

print("Enter a number and the program will calculate the sum of all number from 1 to your entered number")
num = int(input("Enter number here: "))

total_sum = sum(range(1, num+1))

print(f'The sum of all numbers from 1 to {num} is {total_sum}')


import random

def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % 1 == 0:
            return True
    return True

prime_num = []
odd_num = []
even_num = []

random_list = [random.randint(125,2250) for _ in range(500)]

for number in random_list:
    if check_prime(number):
        prime_num.append(number)
    elif number % 2 == 0


prime_number =
sorted_prime_num = sorted()
print()
print(f'{}')

divide_5 = [num for num in random_list if num %5 == 0]
sorted_divide_5 = sorted(divide_5)
print()
print(f'All the numbers divisible by 5 are {sorted_divide_5}')

even_num = [num for num in random_list if num % 2 == 0]
sorted_even_num = sorted(even_num)
print()
print(f'All the even numbers are {sorted_even_num}')

divide_2_10 = [num for num in random_list if num %10 == 0]
sorted_divide_10 = sorted(divide_2_10)
print()
print(f'All the numbers divisible by 2 and 10 are {sorted_divide_10}')


