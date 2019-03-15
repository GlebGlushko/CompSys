import matplotlib.pyplot as plot
import numpy as np
import math
import os

files_paths = {'vinnyk.txt'}
alphabet = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
alphabet_size = len(alphabet)


def display_plot_per_letter(freq):
    # plot.subplot(212)
    plot.figure(figsize=(10, 5))
    plot.bar(x=alphabet, height=freq)
    plot.show()


def calculate_frequency(text_in):
    # print("file_size = ", some_size)
    text = ""
    for x in text_in:
        text += str(x)
    letters_count = 0
    symbols_count = 0
    freq = np.zeros(alphabet_size, dtype='int')
    for symb in text:
        pos = -1
        try:
            pos = alphabet.index(symb)
        except ValueError:
            pass
        if pos != -1:
            freq[pos] += 1
            letters_count += 1
        symbols_count += 1
    return (freq, letters_count, symbols_count)


def calculate_entropy(freq, letters_count):
    entropy = 0
    for x in freq:
        if x > 0:
            entropy -= x / letters_count * math.log2(x / letters_count)
    return entropy


def compare_file_size(file_size, entropy, letters_count, symbols_count):
    print("entropy = {1},\nletters_count = {2},\ntotal_symbols_count = {3},\nfile size = {0},".
          format(file_size, entropy, letters_count, symbols_count))
    print("predicted_file_size = {0},".format(entropy * symbols_count/8))
    print("average_size(2bytes=1ukr_letter&enter,1bytes=other_symbols) = {0},"
          .format(entropy * (letters_count/4 + (symbols_count-letters_count)/8)))


if __name__ == '__main__':
    for path in files_paths:
        print(path)
        file = open(path, "r", encoding='utf-8', errors='ignore')
        entropy_data = calculate_frequency(file.readlines())
        compare_file_size(os.stat(path).st_size, calculate_entropy(entropy_data[0], entropy_data[1]), entropy_data[1],
                          entropy_data[2])
        display_plot_per_letter(calculate_entropy(entropy_data[0], entropy_data[1]))




