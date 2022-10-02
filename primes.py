"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []

    current_number = 2
    while len(list) < number_of_primes:
        prime_flag = True
        for i in range(2, int(current_number / 2) + 1):
            if current_number % i == 0:
                prime_flag = False
        if prime_flag:
            list.append(current_number)
        current_number = current_number + 1

    return list
