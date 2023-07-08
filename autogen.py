import logging
import datetime as dt
import os
import sys
from functions.generator import RandomNumberGenerator

logging.basicConfig(level=logging.INFO)

if len(sys.argv) <= 1:
    raise AttributeError('No arguments found')
logging.info(f"Arguments: {', '.join(sys.argv[1:])}")

curr_date = sys.argv[1]
if isinstance(curr_date, str):
    curr_date = dt.datetime.strftime(curr_date, '%Y-%m-%d %H:%m:%s')
elif isinstance(curr_date, dt.date):
    curr_date = dt.datetime(curr_date)

logging.info(f"Running at {curr_date}")
rng = RandomNumberGenerator(n=5)
numbers = rng.generate_random_numbers(lower_bound=1, upper_bound=100)
for i in range(len(numbers)):
    logging.info(f'Number in order {i} is {numbers[i]}')

logging.info('Iteration completed!')