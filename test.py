"""test.py: Test example to obtain the most frequent letters of a text file
    through the Misra & Gries algorithm for frequency estimation."""

__author__ = "Rafael Sá, 104552, rafael.sa@ua.pt, MEI"

import time

from frequent_count import FrequentCount
from file_processing import get_data_stream
from exact_counts import ExactCount


def get_items_above_threshold(items, k_value):
    threshold = sum(items.values()) / k_value
    res = {}
    for item, value in items.items():
        if value > threshold:
            res[item] = value
    return res


filenames = [
    ["books/The Adventures of Sherlock Holmes.txt", "books/exact counts/The Adventures of Sherlock Holmes.txt"],
    ["books/King James Bible.txt", "books/exact counts/King James Bible.txt"]]
filename_results = "results.txt"
filename_results_excel = "results_to_excel.csv"
min_k = 2
exact_counts = ExactCount()
freq = FrequentCount(min_k)
file_results = open(filename_results, "w")

# Generation of exact counts
# filename_exact_counters = "books/exact counts/King James Bible.txt"
# exact_counts.save_counters(get_data_stream("books/King James Bible.txt"), filename_exact_counters)

file_results.write("Results for the Misra & Gries Algorithm for finding frequent items\n\n")
for filename in filenames:
    exact_counts.load_counters(filename[1])
    data_stream = get_data_stream(filename[0])
    file_results.write("\nText File: " + filename[0] + "\n")
    file_results.write("Exact counts: " + str(exact_counts.get_top_counters(len(exact_counts))) + "\n")
    file_results.write("Number of items: " + str(len(data_stream)) + "\n")
    file_results.write("Number of distinct items: " + str(len(exact_counts)) + "\n")
    for k in range(min_k, len(exact_counts)):
        freq.update_k(k)
        file_results.write("k: " + str(k) + ":\n")
        start = time.time()
        result = freq.get_frequent_items(data_stream)
        end = time.time()
        result = sorted(result.items(), key=lambda x: x[1], reverse=True)  # Ordered by frequency
        exact_count = exact_counts.get_top_counters(len(result))
        total_exact_count = exact_counts.get_exact_counters()
        same_position = 0
        sum_exact = 0
        sum_dif = 0
        sum_percentage_dif = 0
        sum_must_have = 0
        must_items = get_items_above_threshold(total_exact_count, k)
        for i in range(len(result)):
            if result[i][0] in must_items:
                sum_must_have += 1
            if exact_count[i][0] == result[i][0]:
                same_position += 1
            sum_dif += total_exact_count[result[i][0]] - result[i][1]
            sum_exact += total_exact_count[result[i][0]]
            sum_percentage_dif += ((total_exact_count[result[i][0]] - result[i][1]) * 100) / total_exact_count[result[i][0]]
        percentage_pos = (same_position / len(result)) * 100
        percentage_dif = sum_percentage_dif / len(result)
        percentage_must_have = 100.0
        if len(must_items) > 0:
            percentage_must_have = (sum_must_have / len(must_items)) * 100
        file_results.write("\tResults: " + str(result) + "\n")
        file_results.write(f"\tPercentage of items in the same position: {percentage_pos:.2f}%\n")
        file_results.write("\tSum of the differences between the exact counter and the estimate: " + str(sum_dif) + "\n")
        file_results.write(f"\tMean of the percentage of the difference between the exact counter and the estimate: {percentage_dif:.2f}%\n")
        file_results.write(f"\tPercentage of items with frequency greater than m/k: {percentage_must_have:.2f}%\n")
        file_results.write(f"\tExecution time: {(end - start):.2f} seconds\n")
file_results.close()
print("\nResults written to the file: \"" + filename_results + "\"")
