import matplotlib.pyplot as plot
import numpy as np
import math
import  os
files_paths = {'vinnyk.txt'}
alphabet = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')
#alphabet_upper = list('АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ')
alphabet_size = len(alphabet)


def display_plot_per_letter(freq):
    # plot.subplot(212)
    plot.figure(figsize=(10, 5))
    plot.bar(x=alphabet, height=freq)
    plot.show()

def calculate_frequency(text, some_size):
    print("file_size = ", some_size)
    text = str(text).lower()
    letters_count = 0
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
    #display_plot_per_letter(freq)
    print("letters count = ", letters_count)
    calculate_enthropy(freq)


def calculate_enthropy(freq):
    entropy = 0
    for x in freq:
        if x > 0:
            entropy += x/alphabet_size * math.log2(1./(x/alphabet_size))
    print(entropy)

if __name__ == '__main__':
    for path in files_paths:
        print(path)
        file = open(path, "r", encoding='utf-8', errors='ignore')
        calculate_frequency(file.readlines(), os.stat(path).st_size)
