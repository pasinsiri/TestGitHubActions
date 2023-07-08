import logging
import os
import sys
from functions.generator import RandomNumberGenerator


if len(sys.argv) == 0:
    raise AttributeError('No arguments found')

curr_date = sys.argv[0]
logging.info(f'Running at ')
rng = RandomNumberGenerator(n=5)
numbers = rng.generate_random_numbers(lower_bound=1, upper_bound=100)
for i in range(numbers):
    logging.info(f'Number in order {i} is {numbers[i]}')

logging.info('Iteration completed!')