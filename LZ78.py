import numpy as np
from random import randint
import matplotlib.pyplot as plt
import mylib
from bitarray import bitarray
from math import *


def tauxcomp_LZ78(phrase, couple):
    taille_orig = len(phrase)*8
    couple_trie = sorted(couple, key=lambda x: x[1])
    bit_min = np.round(log(couple_trie[-1][1], 2)+.5)
    taille_LZ78 = len(couple)+(bit_min+8)
    return round((1-(taille_LZ78/taille_orig))*100, 2)


def LZ78_encode(seq):
    code = []
    liste = []
    char = ''
    j = 0
    for i in seq:
        char += i
        if char not in liste:
            liste.append(char)
            if len(char) == 1:
                code.append(chr(0))
                code.append(char)
                char = ''
            else:
                j = liste.index(char[:-1])+1
                code.append(chr(j))
                code.append(char[-1])
                char = ''
    return code


def LZ78_decode(seq):
    liste_symb = []
    char = ''
    for i in range(0, len(seq), 2):
        if str(ord(seq[i])) == '0':
            liste_symb.append(seq[i+1])
        else:
            index = int(ord(seq[i]))-1
            char = liste_symb[index]+seq[i+1]
            liste_symb.append(char)
    return ''.join(liste_symb)


if __name__ == "__main__":

    # ---------------------------- gray image Test ----------------------------

    # generate gray image
    image_gray = mylib.gen_mat_gray(10, 10)

    image_gray = mylib.gen_mat_gray(10, 10)
    plt.imshow(image_gray, cmap=plt.get_cmap('gray'))
    sequence = mylib.Img2liste_row(image_gray)
    newliste = [chr(i) for i in sequence]
    lzw_image = LZ78_encode(newliste)
    print(lzw_image)

    decode = LZ78_decode(lzw_image)
    newliste = [ord(i) for i in decode]
    plt.imshow(mylib.liste2img_row(newliste, 10, 10),
               cmap=plt.get_cmap('gray'))
