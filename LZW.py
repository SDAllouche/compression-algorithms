import numpy as np
from random import randint
import matplotlib.pyplot as plt
import mylib
from bitarray import bitarray


def LZW_encode(seq):
    # craete ascci dictionary
    code = dict((chr(i), i) for i in range(256))

    # first caracteres in string
    previous = seq[0]

    # add new caracters into dictionary
    liste = []
    for i in seq[1:]:
        if previous+i in code:
            previous += i
        else:
            liste.append(code[previous])
            code[previous+i] = len(code)
            previous = i

    # append the last caracters
    liste.append(code[previous])

    return liste


def LZW_decode(seq):
    # craete ascci dictionary
    code = dict((i, chr(i)) for i in range(256))

    liste = []
    # first caracters
    previous = code[seq[0]]
    # append first caracters
    liste.append(previous)

    # add new caracters into dictionary and decode in the same time
    for i in seq[1:]:
        if i not in code:
            char = previous+previous[0]
        else:
            char = code[i]
        liste.append(char)
        code[len(code)] = previous+char[0]
        previous = char

    return ''.join(liste)


if __name__ == "__main__":

    # ---------------------------- Chain Test ----------------------------

    se = 'veridique ! dominique pique nique en tunique'
    lzw = LZW_encode(se)
    print(lzw)

    print(LZW_decode(lzw))

    # ---------------------------- gray image Test ----------------------------

    # generate gray image
    image_gray = mylib.gen_mat_gray(10, 10)

    image_gray = mylib.gen_mat_gray(10, 10)
    plt.imshow(image_gray, cmap=plt.get_cmap('gray'))
    sequence = mylib.Img2liste_row(image_gray)
    newliste = [chr(i) for i in sequence]
    lzw_image = LZW_encode(newliste)
    print(lzw_image)

    decode = LZW_decode(lzw_image)
    newliste = [ord(i) for i in decode]
    plt.imshow(mylib.liste2img_row(newliste, 10, 10),
               cmap=plt.get_cmap('gray'))
