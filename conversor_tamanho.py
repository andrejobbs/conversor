# from skimage.transform import resize
# import matplotlib.pyplot as plt
# import os

# imagens = os.listdir("/home/andre/Documentos/estudos_python/conversor_img/imagens")


# for i in imagens:
#         imagem = plt.imread(f"imagens/{i}")
#         resolucao = resize(imagem, (500, 500))
        
# from tkinter import Image
# from PIL import ImageDraw

# imagem = Image.open('/home/andre/Documentos/estudos_python/conversor_img/imagem_1000x1000/2472396.png')
# imagem.show()


from PIL import Image
import os
imagens = os.listdir("imagem_1000x1000")
for arq in imagens:
    opcao = str(input(f"Deseja redimensionar essa imagem :{arq}\n S/s-> Para converter \n"))
    if opcao=='s' or opcao=='S':
        x=int(input("Insira um valor para largura:"))
        y=int(input("Insira um valor para altura:"))
        img=Image.open(f"imagem_1000x1000/{arq}").convert("RGB")
        novoFormato = img.resize((x, y))
        novoFormato.save(f'imagem_redimensionada/{arq} {arq.replace("png","jpg")}')
    else:
        continue
