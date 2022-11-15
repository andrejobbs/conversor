from PIL import Image
import os
imagens=os.listdir("imagens")
for arquivo in imagens:
    img= Image.open(f"imagens/{arquivo}").convert("RGB")
    print('As imagens principais se encontram no formato JPG...')
    print('1.para converte-las em PNG')
    print('2.para converte-las em TIFF')
    op=int(input('Insira sua opção:'))
    if op==1:
        img.save(f'imagens_png/{arquivo.replace("jpg","png")}')
        print(f'A imgem {arquivo} foi salva em png')
    elif op==2:
        img.save(f'imagens_tiff/{arquivo.replace("jpg","tiff")}')
        print(f'A imgem {arquivo} foi salva em tiff')
    else:
        print('Opção não encontrada')    