import logging
import datetime as dt
import time
import os
import sys
from functions.generator import RandomNumberGenerator

logging.basicConfig(level=logging.INFO)

curr_time = dt.datetime.now()
curr_date = curr_time.date()
logging.info(f"Running at {curr_date}")
rng = RandomNumberGenerator(n=5)
numbers = rng.generate_random_numbers(lower_bound=1, upper_bound=100)
for i in range(len(numbers)):
    logging.info(f'Number in order {i} is {numbers[i]}')

logging.info('Iteration completed!')