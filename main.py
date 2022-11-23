import cv2
import matplotlib.pyplot as plt
import numpy as np


def main():
    imagem = cv2.imread('imagens/bike.png', 0)
    imagemBinarizada = np.array(imagem)
    t = int(input("Informe o valor T(Ponto de divisão entre Branco e Preto): "))
    binarizarImagem(imagem, imagemBinarizada, t)
    mostrarHistogramas(imagem, imagemBinarizada)
    mostrarImagens(imagem, imagemBinarizada)

    linha, coluna = imagem.shape
    matrizComBordas = np.zeros((linha + 2, coluna + 2))

    mascara = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])

    criarMatrizComBordasZeradas(matrizComBordas, imagemBinarizada, mascara)


def binarizarImagem(imagem, imagemBinarizada, t):
    linha, coluna = imagem.shape
    for i in range(linha):
        for j in range(coluna):
            if imagem[i, j] < t:
                imagemBinarizada[i, j] = 0
            else:
                imagemBinarizada[i, j] = 255


def mostrarHistogramas(original, alterada):
    plt.subplot(121)
    plt.title('Histograma Original')
    plt.xlabel('Niveis de Cinza')
    plt.ylabel('Qtde de Pixels')
    plt.hist(original.ravel(), 256, [0, 255])

    plt.subplot(122)
    plt.title('Histograma Binarizado')
    plt.xlabel('Niveis de Cinza')
    plt.ylabel('Qtde de Pixels')
    plt.hist(alterada.ravel(), 256, [0, 255])

    plt.show()


def mostrarImagens(original, alterada):
    cv2.imshow('Imagem Original', original)
    cv2.imshow('Imagem Binarizada', alterada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def criarMatrizComBordasZeradas(arrayComBordas, imagemBinarizada, mascara):
    linha, coluna = imagemBinarizada.shape
    for i in range(linha):
        for j in range(coluna):
            arrayComBordas[i + 1][j + 1] = imagemBinarizada[i][j]

    linha, coluna = imagemBinarizada.shape
    for i in range(linha):
        for j in range(coluna):
            imagemBinarizada[i][j] = \
                (arrayComBordas[i - 1][j - 1] * mascara[0][0]) \
                + (arrayComBordas[i - 1][j] * mascara[0][1]) \
                + (arrayComBordas[i - 1][j + 1] * mascara[0][2]) \
                + (arrayComBordas[i][j - 1] * mascara[1][0]) \
                + (arrayComBordas[i][j] * mascara[1][1]) \
                + (arrayComBordas[i][j + 1] * mascara[1][2]) \
                + (arrayComBordas[i + 1][j - 1] * mascara[2][0]) \
                + (arrayComBordas[i + 1][j] * mascara[2][1]) \
                + (arrayComBordas[i + 1][j + 1] * mascara[2][2])
            imagemBinarizada[i][j]/=2

    print(arrayComBordas)
    print(imagemBinarizada)
    mostrarImagens(arrayComBordas, imagemBinarizada)


main()
