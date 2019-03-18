import matplotlib.pyplot as plt
import numpy as np
import math
import os

files_paths = {'docker.txt'}


def display_plot_per_letter(freq, alphabet):
    # plot.subplot(212)

    plt.figure(figsize=(10, 5))
    plt.bar(x=alphabet, height=freq)
    plt.show()


def calculate_frequency(text_in, alphabet):

    # print("file_size = ", some_size)
    text = ""
    for x in text_in:
        text += str(x)
    letters_count = 0
    symbols_count = 0
    freq = np.zeros(len(alphabet), dtype='int')
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
    print("predicted_file_size = {0},".format(entropy * letters_count/2))
    # print("average_size(2bytes=1ukr_letter&enter,1bytes=other_symbols) = {0},"
    #       .format(entropy * (letters_count/4 + (symbols_count-letters_count)/8)))


archive_name = ('orginal', 'rar', 'zip', '7-zip','PeaZip')
archive_size_docker = (11675, 3809, 3961, 3643, 3953)
archive_size_weed = (7381, 2551, 2616, 2480, 2556)
archive_size_vinnyk = (1464, 533, 533, 555, 542)
fn = ('docker', 'weed', 'vinnyk')
ao = (11675, 7381, 1464)
ar = (3809, 2551, 533)
az = (3961, 2616, 533)
a7 = (3643, 2480, 555)
ap = (3953, 2556, 542)


def display_plot_per_archive():

    fig, ax = plt.subplots()
    index = np.arange(3, 10, 3)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index - 2*bar_width, ao, bar_width,
                     alpha=opacity,
                     color='b',
                     label='originl')

    rects2 = plt.bar(index - bar_width, ar, bar_width,
                     alpha=opacity,
                     color='g',
                     label='rar')
    rects3 = plt.bar(index, az, bar_width,
                     alpha=opacity,
                     color='r',
                     label='zip')
    rects4 = plt.bar(index + bar_width, a7, bar_width,
                      alpha=opacity,
                      color='y',
                      label='7-zip')
    rects5 = plt.bar(index + 2*bar_width, ap, bar_width,
                      alpha=opacity,
                      color='black',
                      label='peazip')

    plt.xticks(index, fn)
    plt.legend()
    plt.show()

if __name__ == '__main__':
    for path in files_paths:
        print(path)
        alphabet = list('абвгґдеєжзиіїйклмнопрстуфхцчшщьюя')

        file = open(path, "r", encoding='utf-8', errors='ignore')
        entropy_data = calculate_frequency(file.readlines(), alphabet)
        compare_file_size(os.stat(path).st_size, calculate_entropy(entropy_data[0], entropy_data[1]), entropy_data[1],
                          entropy_data[2])
        # display_plot_per_letter(entropy_data[0], alphabet)
        display_plot_per_archive()


