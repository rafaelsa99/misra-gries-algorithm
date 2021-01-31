"""test.py: Test example to obtain the most frequent letters of a text file
    through the Misra & Gries algorithm for frequency estimation."""

__author__ = "Rafael Sá, 104552, rafael.sa@ua.pt, MEI"

from frequent_count import FrequentCount
from file_processing import get_data_stream
from exact_counts import ExactCount

filename = "books/The Adventures of Sherlock Holmes.txt"
data_stream = get_data_stream(filename)

exact_counts = ExactCount()
exact_counts.load_counters("books/counters.txt")
print(exact_counts.get_exact_counters())

freq = FrequentCount(3)
print(freq.get_frequent_items(data_stream))
