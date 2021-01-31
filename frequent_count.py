"""frequent_count.py: Implementation of the Misra & Gries algorithm
    to obtain an estimate of the most frequent letters."""

__author__ = "Rafael Sá, 104552, rafael.sa@ua.pt, MEI"


class FrequentCount(object):

    def __init__(self, k):
        """
        :param k: Controls the quality of the results given
        """
        if k > 0:
            self.k = k
        else:
            raise ValueError("The parameter k must be a positive integer.")
        self.freq_items = {}

    def update_k(self, k):
        """Updates the value of the parameter k."""
        if k > 0:
            self.k = k

    def get_frequent_items(self, sequence):
        """Returns the frequent items of a given data stream."""
        self.freq_items = {}
        for char in sequence:
            self.process_item(char)
        return self.freq_items

    def process_item(self, char):
        """Adds or increases the counter of an item or, if there is no space for new counters,
         decreases and deletes the existing counters."""
        if char in self.freq_items:
            self.freq_items[char] += 1
        elif len(self.freq_items) < self.get_max_counters():
            self.freq_items[char] = 1
        else:
            self.decrement_and_delete_counters()

    def decrement_and_delete_counters(self):
        """Decreases all counters and deletes the counters equal to zero."""
        for item in list(self.freq_items):
            self.freq_items[item] -= 1
            if self.freq_items[item] == 0:
                del self.freq_items[item]

    def get_max_counters(self):
        """Returns the maximum number of counters that can exist at any time."""
        return self.k - 1

    def __getitem__(self, item):
        """Returns an estimate for the number of occurrences of a given item."""
        if item in self.freq_items:
            return self.freq_items[item]
        else:
            return 0

    def __len__(self):
        """Returns the number of frequent items with counters."""
        return len(self.freq_items)
