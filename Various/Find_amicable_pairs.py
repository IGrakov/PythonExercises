# Two numbers are considered to be amicable or friendly if the first is equal to the sum of divisors of the second,
# and if the second number is equal to the sum of divisors of the first.
# Write a function find_amicable_pairs that takes an integer and returns number of amicable pairs and
# list of tuples of such amicable pairs found in the range from 0 to the given integer.
# For example:
# find_amicable_pairs(10) => 0
# find_amicable_pairs(230) => 1 // (220, 284)
# find_amicable_pairs(6000) => 4 // all the above plus (1184, 1210), (2620, 2924), (5020, 5564)
# find_amicable_pairs(10000) => 5 // all the above plus (6232, 6368)
# find_amicable_pairs(20000) => 8 // all the above plus (10744, 10856), (12285, 14595), (17296, 18416)


def find_divisors(num: int) -> list:
    divisors = [1]
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def find_amicable_pairs(num: int) -> tuple:

    if type(num) != int:
        raise TypeError("Argument must be of int type")

    count = 0
    amicable_numbers = set()
    amicable_pairs = []

    for first_num in range(num):
        second_num = sum(find_divisors(first_num))

        # Skip the same number or previously found amicable number
        if second_num == first_num or first_num in amicable_numbers:
            continue

        second_num_divisors_sum = sum(find_divisors(second_num))

        if second_num_divisors_sum == first_num:
            amicable_numbers.add(second_num)
            amicable_pairs.append((first_num, second_num))
            count += 1

    return count, amicable_pairs
