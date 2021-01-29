"""Frequency_Estimation.py: Implementation of the Misra & Gies algorithm
    to obtain an estimate of the most frequent letters."""

__author__ = "Rafael Sá, 104552, rafael.sa@ua.pt, MEI"


class FrequencyEstimation(object):

    def __init__(self, k):
        if k > 0:
            self.k = k
        else:
            raise ValueError("The size of the array, k, must be a positive integer.")
        self.freq_items = {}

    def count_frequent_items(self, sequence):
        self.freq_items = {}
        for char in sequence:
            if char.isalpha():  # Is really necessary?
                if char in self.freq_items:
                    self.freq_items[char] += 1
                elif len(self.freq_items) < (self.k - 1):
                    self.freq_items[char] = 1
                else:
                    for item in list(self.freq_items):
                        self.freq_items[item] -= 1
                        if self.freq_items[item] == 0:
                            del self.freq_items[item]
        return self.freq_items

    def __getitem__(self, item):
        if item in self.freq_items:
            return self.freq_items[item]
        else:
            return 0
