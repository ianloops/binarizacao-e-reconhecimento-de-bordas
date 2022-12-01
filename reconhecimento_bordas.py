def reconhecerBordas(imagemAlterada, matrizAuxiliar, mascara):
    linha, coluna = imagemAlterada.shape
    for i in range(linha):
        for j in range(coluna):
            matrizAuxiliar[i + 1][j + 1] = imagemAlterada[i][j]

    linha, coluna = imagemAlterada.shape
    for i in range(linha):
        for j in range(coluna):
            imagemAlterada[i][j] = \
                (matrizAuxiliar[i - 1][j - 1] * mascara[0][0]) \
                + (matrizAuxiliar[i - 1][j] * mascara[0][1]) \
                + (matrizAuxiliar[i - 1][j + 1] * mascara[0][2]) \
                + (matrizAuxiliar[i][j - 1] * mascara[1][0]) \
                + (matrizAuxiliar[i][j] * mascara[1][1]) \
                + (matrizAuxiliar[i][j + 1] * mascara[1][2]) \
                + (matrizAuxiliar[i + 1][j - 1] * mascara[2][0]) \
                + (matrizAuxiliar[i + 1][j] * mascara[2][1]) \
                + (matrizAuxiliar[i + 1][j + 1] * mascara[2][2])
            imagemAlterada[i][j]
