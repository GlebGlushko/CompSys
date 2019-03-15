def tobase64(s):
    b64s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    # b64p = "="
    ret = ""
    left = 0
    for i in range(0, len(s)):
        if left == 0:
            ret += b64s[ord(s[i]) >> 2]
            left = 2
        else:
            if left == 6:
                ret += b64s[ord(s[i-1]) & 63]
                ret += b64s[ord(s[i]) >> 2]
                left = 2
            else:
                index1 = ord(s[i-1]) & (2 ** left - 1)
                index2 = ord(s[i]) >> (left + 2)
                index = (index1 << (6 - left)) | index2
                ret += b64s[index]
                left += 2
    if left != 0:
        ret += b64s[(ord(s[len(s) - 1]) & (2 ** left - 1)) << (6 - left)]
    return ret


def print_ord(s):
    for x in s:
        print(x)
        #print(x, ' ', ord(x))

if __name__ == '__main__':
    #print("ukraine")
    txt = 'я'.encode(encoding="windows-1251")
    print(print_ord(txt))

