import random 
import csv
import logging

class RandomNumberGenerator:
    def __init__(self, n) -> None:
        self.n = n 

    def generate_random_numbers(self, lower_bound, upper_bound):
        random_numbers = []
        for _ in range(self.n):
            random_numbers.append(random.randint(lower_bound, upper_bound))
        return random_numbers

    def write_csv_from_lists(self, data_lists, column_names, export_path):
        if len(data_lists) == 0:
            return
        
        # Get the data and column names for the first list
        data = data_lists[0]
        names = column_names[0]

        if len(data) == 0:
            return

        # Create a new CSV file
        with open(export_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write the column names
            writer.writerow(names)
            
            # Write the data rows
            for row in data:
                writer.writerow(row)
        
        logging.info("CSV file created successfully!")
