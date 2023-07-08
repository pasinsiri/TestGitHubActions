import logging
import datetime as dt
import os
import sys
from functions.generator import RandomNumberGenerator

logging.basicConfig(level=logging.INFO)

if len(sys.argv) <= 1:
    raise AttributeError('No arguments found')

curr_date = sys.argv[1]
logging.info(f"Running at {dt.datetime.strftime(curr_date, '%Y-%m-%d %H:%m:%s')}")
rng = RandomNumberGenerator(n=5)
numbers = rng.generate_random_numbers(lower_bound=1, upper_bound=100)
for i in range(len(numbers)):
    logging.info(f'Number in order {i} is {numbers[i]}')

logging.info('Iteration completed!')