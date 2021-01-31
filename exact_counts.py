"""exact_counts.py: Module that handles the exact counts of a text file."""

__author__ = "Rafael Sá, 104552, rafael.sa@ua.pt, MEI"

import ast
from file_processing import write_dict_to_file


class ExactCount(object):

    def __init__(self):
        self.counters = {}

    def get_exact_counters(self):
        """Returns the exact counts of the frequency of the items."""
        return self.counters

    def load_counters(self, filename):
        """Load exact counter from file"""
        with open(filename, 'r') as file:
            data = file.read()
        self.counters = ast.literal_eval(data)

    def save_counters(self, sequence, filename):
        """Get the counters and saves in a file."""
        self.count_items_frequency(sequence)
        write_dict_to_file(self.counters, filename)

    def count_items_frequency(self, sequence):
        """Count the frequency of the items in the sequence."""
        self.counters = {}
        for char in sequence:
            if char in self.counters:
                self.counters[char] += 1
            else:
                self.counters[char] = 1

    def __getitem__(self, item):
        """Returns the counter of a given item."""
        if item in self.counters:
            return self.counters[item]
        else:
            return 0

    def __len__(self):
        """Returns the number of items with counters."""
        return len(self.counters)
