

def binarizarImagem(imagem, imagemAlterada, t):
    linha, coluna = imagem.shape
    for i in range(linha):
        for j in range(coluna):
            if imagem[i, j] < t:
                imagemAlterada[i, j] = 0
            else:
                imagemAlterada[i, j] = 255
