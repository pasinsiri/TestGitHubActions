import logging
from functions.generator import RandomNumberGenerator

rng = RandomNumberGenerator(n=5)
numbers = rng.generate_random_numbers(lower_bound=1, upper_bound=100)
for i in range(numbers):
    logging.info(f'Number in order {i} is {numbers[i]}')

logging.info('Iteration completed!')