import numpy as np
from random import randint
import matplotlib.pyplot as plt
import mylib
from bitarray import bitarray


def RLE_encode(chaine):

    # convert chaine to liste of caracters
    liste = []
    liste[:0] = chaine

    # Add -1 at first and end
    liste = np.concatenate([[-1], liste, [-1]])

    # determine the index of where there is change of value
    index = np.where(liste[1:] != liste[:-1])[0] + 1

    # calculate difference between two succissive variable in liste
    difference = np.diff(index)

    return np.concatenate([[difference[i], liste[index[i]]] for i in range(len(difference))])


def Taux(serie, code):
    return ((len(serie)-len(code))/len(serie))*100


def RLE_decode(liste):
    return ''.join([int(liste[i])*str(liste[i+1]) for i in range(0, len(liste), 2)])


if __name__ == "__main__":

    # ---------------------------- Chain Test ----------------------------

    serie = input()
    rle = RLE_encode(serie)
    print(rle)

    print(Taux(serie, rle))

    print(RLE_decode(rle))

    # ---------------------------- Black-white image Test ----------------------------

    img = np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

    nl, nc = img.shape
    seq = mylib.Img2liste_row(img)
    codage = RLE_encode(seq)
    decodage = RLE_decode(codage)
    print("Codage : ", codage)
    print("Decodage : ", decodage)
    serie = []
    serie[:0] = decodage
    image = mylib.liste2img_row(serie, nl, nc)
    plt.imshow(image, cmap=plt.get_cmap('gray'))

    # ---------------------------- gray image Test ----------------------------

    # generate gray image
    image_gray = mylib.gen_mat_gray(10, 10)

    nl, nc = image_gray.shape
    sequence = mylib.Img2liste_row(image_gray)
    seq = [chr(i) for i in sequence]
    codage = RLE_encode(seq)
    decodage = RLE_decode(codage)
    print("Codage : ", codage)
    print("Decodage : ", decodage)
    serie = [ord(i) for i in decodage]
    new_image = mylib.liste2img_row(serie, nl, nc)
    plt.imshow(new_image, cmap=plt.get_cmap('gray'))
