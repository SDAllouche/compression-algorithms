from collections import defaultdict
from heapq import heappush, heappop, heapify
import numpy as np
from random import randint
import matplotlib.pyplot as plt
import mylib
from bitarray import bitarray
from math import *
from tabulate import tabulate


def tauxcomp(L, V):
    return round((len(V)/(len(L)*8))*100, 2)


def evalue(seq, dic, dichuff):
    moyenne = 0
    entropie = 0
    for i, j in dic.items():
        moyenne += len(dichuff[i])*(j/len(seq))
        entropie += (j/len(seq))*log(1/(j/len(seq)), 2)
    rend = entropie/(moyenne*log(len(seq), 2))
    return moyenne, entropie, entropie/moyenne, rend


def freqoccur(seq):
    return dict((i, seq.count(i)) for i in set(seq))


def Huffman_encode(dictionary):

    # create default dictionary
    tree = [[fq, [sym, ""]] for sym, fq in dictionary.items()]

    # give dictionary the shpae of tree
    heapify(tree)

    while len(tree) > 1:
        # Pop and return the smallest item from the tree
        left = heappop(tree)
        right = heappop(tree)

        for pair in left[1:]:
            # add zero to all the right note
            pair[1] = '0' + pair[1]
        for pair in right[1:]:
            # add one to all the left note
            pair[1] = '1' + pair[1]

        # add new node in tree
        heappush(tree, [left[0] + right[0]] + left[1:] + right[1:])

    return left[1:] + right[1:]


def Huffman_decode(data, huffman_dict):

    # decode data using huffman dictinary
    data = data.decode(huffman_dict)

    return ''.join(data)


if __name__ == "__main__":

    seq = "maman et mammy mangent ma mangue avec engouement"
    dictionary = freqoccur(seq)
    print(dictionary)
    print("Nombre de caractere deffirents : ", len(dictionary))
    print("Les 3 caractere les plus representes : ",
          max(dictionary, key=dictionary.get))

    # ---------------------------- Chain Test ----------------------------

    data = bitarray()
    huffman = Huffman_encode(dictionary)
    huffman_dictionary = {a[0]: bitarray(a[1]) for a in huffman}
    data.encode(huffman_dictionary, seq)
    print(huffman_dictionary)

    print(Huffman_decode(data, huffman_dictionary))

    # ---------------------------- gray image Test ----------------------------

    # generate gray image
    image_gray = mylib.gen_mat_gray(10, 10)

    image_gray = mylib.gen_mat_gray(10, 10)
    plt.imshow(image_gray, cmap=plt.get_cmap('gray'))
    sequence = mylib.Img2liste_row(image_gray)
    newliste = [chr(i) for i in sequence]
    data_img = bitarray()
    dictionary_img = freqoccur(newliste)
    huffman_img = Huffman_encode(dictionary_img)
    huffman_dictionary_img = {a[0]: bitarray(a[1]) for a in huffman_img}
    data_img.encode(huffman_dictionary_img, newliste)
    print(huffman_dictionary_img)

    decode = Huffman_decode(data_img, huffman_dictionary_img)
    newliste = [ord(i) for i in decode]
    plt.imshow(mylib.liste2img_row(newliste, 10, 10),
               cmap=plt.get_cmap('gray'))

    print(evalue(seq, dictionary, huffman_dictionary))

    data = [[i.upper(), dictionary[i], dictionary[i]/len(seq), ord(i), j, len(j)]
            for i, j in huffman_dictionary.items()]
    column = ["Caractere", "Occurence", "Frequence",
              "Code Ascii", "Code Huffman", "Longueur"]
    print(tabulate(data, headers=column, tablefmt="fancy_grid"))
