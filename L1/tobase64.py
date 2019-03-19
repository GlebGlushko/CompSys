import base64
from main import *
import sys
import os
from pathlib import Path

b64s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def tobase64(s):
    bs = ''
    res = ''
    for x in s:
        bs += str(bin(int.from_bytes(bytearray(x, 'utf-8'), byteorder='big')))[2:].zfill(8)
        while len(bs) >= 6:
            res += b64s[int(bs[:6], 2)]
            bs = bs[6:]
    kol =0
    if len(bs) > 0:
        while len(bs) < 6:
            kol += 1
            bs += '0'
        res += b64s[int(bs[:6], 2)]
    res += '=' * int(kol/2)
    return res

def btob64(s):
    bs = ''
    res = ''

    for x in s:
        bs += str(bin(x))[2:].zfill(8)
        while len(bs) >= 6:
            res += b64s[int(bs[:6], 2)]
            bs = bs[6:]
    kol = 0
    if len(bs) > 0:
        while len(bs) < 6:
            kol += 1
            bs += '0'
        res += b64s[int(bs[:6], 2)]
    res += '=' * int(kol / 2)
    return res


if __name__ == '__main__':
    path = "src/docker.rar"
    print(path)
    file = Path(path).read_bytes()
    # print(os.stat(path).st_size)
    # print(file)
    txt64 = (btob64(file))
    alphabet = list('abcdefghijklmnopqrstuvwxyz0123456789+/')
    alphabet_size = len(alphabet)
    entropy_data = calculate_frequency(txt64, alphabet)
    compare_file_size(os.stat(path).st_size, calculate_entropy(entropy_data[0], entropy_data[1]), entropy_data[1],
                      entropy_data[2])

    display_plot_per_letter(entropy_data[0], alphabet)

    exit()
    txt = ''
    for x in file:
        txt += x
    # txt = "Слава Україні!!"
    txt.encode(encoding='utf-8')
    libtxt64 = str(base64.b64encode(bytes(txt,encoding='utf-8')))[2:-1]
    txt64 = tobase64(txt)
    # print('input: ', txt)
    # print('my result:  ', txt64)
    # print('lib result: ', libtxt64)
    print(path)
    print(txt64 == libtxt64)

    alphabet = list('abcdefghijklmnopqrstuvwxyz0123456789+/')
    alphabet_size = len(alphabet)
    entropy_data = calculate_frequency(txt64, alphabet)
    compare_file_size(sys.getsizeof(txt64), calculate_entropy(entropy_data[0], entropy_data[1]), entropy_data[1],
                    entropy_data[2])

    display_plot_per_letter(entropy_data[0], alphabet)

