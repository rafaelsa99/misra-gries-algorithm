"""Frequent_Count.py: Test example to obtain the most frequent letters of a text file
    through the Misra & Gries algorithm for frequency estimation."""

__author__ = "Rafael Sá, 104552, rafael.sa@ua.pt, MEI"

from Frequency_Estimation import FrequencyEstimation as FreqEstimation

freq = FreqEstimation(2)
print(freq.count_frequent_items("adeddedd"))
