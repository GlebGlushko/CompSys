import base64
from main import *
import sys

b64s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
def tobase64(s):
    bs = ''
    res = ''
    for x in s:

        # print(str(bin(int.from_bytes(bytearray(x,'utf-8'), byteorder='big'))), ' this is = ',x,'end')
        bs+= str(bin(int.from_bytes( bytearray(x,'utf-8'), byteorder='big')))[2:].zfill(8)
        while len(bs)>=6:
            res += b64s[int(bs[:6],2)]
            bs = bs[6:]
    if len(bs) > 0:
        while len(bs)<6:
            bs += '0'
        res += b64s[int(bs[:6],2)]

    return res


if __name__ == '__main__':
    #print("ukraine")
    path = "lab.txt"
    file = open(path, "r", encoding='utf-8').readlines()
    txt = ''
    for x in file:
        txt += x
    txt.encode(encoding='utf-8')
    libtxt64 = str(base64.b64encode(bytes(txt,encoding='utf-8')))[2:-1]
    txt64 = tobase64(txt)
    print(txt64)
    print(libtxt64)
    print(txt64 == libtxt64)

    alphabet = list('abcdefghijklmnopqrstuvwxyz0123456789+/')
    alphabet_size = len(alphabet)
    entropy_data = calculate_frequency(txt64, alphabet)
    compare_file_size(sys.getsizeof(txt64), calculate_entropy(entropy_data[0], entropy_data[1]), entropy_data[1],
                      entropy_data[2])

    display_plot_per_letter(entropy_data[0], alphabet)

# 00100000  0000