import cv2
import matplotlib.pyplot as plt
import numpy as np
import binarizacao as bin
import reconhecimento_bordas as recon


def main():
    #Arquivos e Parametros
    arq= "imagens/"+input("Informe qual imagem deseja alterar utilizar:")
    #arq="imagens/moldeDog.jpg"
    imagem = cv2.imread(arq, 0)
    mascara = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])

    #Binarização de Imagem
    imagemAlterada = np.array(imagem)
    mostrarHistogramas(imagem, imagemAlterada)
    t = int(input("Informe o valor T(Ponto de divisão entre Branco e Preto): "))
    bin.binarizarImagem(imagem, imagemAlterada, t)
    mostrarImagens(imagem, imagemAlterada)
    #cv2.imwrite(arq + "binarizada", imagemAlterada)

    #Reconhecimento de Bordas
    linha, coluna = imagem.shape
    matrizAuxiliar = np.zeros((linha + 2, coluna + 2))
    recon.reconhecerBordas(imagemAlterada, matrizAuxiliar, mascara)
    mostrarHistogramas(imagem, imagemAlterada)
    mostrarImagens(imagem, imagemAlterada)
    arq = "imagens/" + input("Como deseja salvar o arquivo?")+".jpg"
    cv2.imwrite(arq, imagemAlterada)



def mostrarHistogramas(original, alterada):
    plt.subplot(121)
    plt.title('Histograma Original')
    plt.xlabel('Niveis de Cinza')
    plt.ylabel('Qtde de Pixels')
    plt.hist(original.ravel(), 256, [0, 255])

    plt.subplot(122)
    plt.title('Histograma Alterado')
    plt.xlabel('Niveis de Cinza')
    plt.ylabel('Qtde de Pixels')
    plt.hist(alterada.ravel(), 256, [0, 255])

    plt.show()


def mostrarImagens(original, alterada):
    cv2.imshow('Imagem Original', original)
    cv2.imshow('Imagem Alterada', alterada)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


main()
