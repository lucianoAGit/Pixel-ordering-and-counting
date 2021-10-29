#Importando Bibliotecas
import cv2
import numpy as np
from glob import glob
import os
import csv

#--------------------------------------------------------
# Carrega todos os arquivos .png da pasta
img_names = glob(os.path.join(os.getcwd(), '*.png'))

#--------------------------------------------------------
#Conta os pixels
with open('Pixels_G2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for fn in img_names:

        img = cv2.imread(fn,0)
        npix = np.sum(img != 0)

        writer.writerow([str(os.path.basename(fn)), str(npix)]) 
              
#--------------------------------------------------------
#Ordena os pacientes de acordo com o n° de pixels

with open ("Pixels_G2.csv", "r") as f:
    dados = csv.reader(f, delimiter=",")
    # Com o arquivo lido pelo módulo csv é possível convertê-lo em uma lista
    lista = list(dados)
    # Ordenação da lista gerada considerando o segundo elemento em ordem decrescente.
    lista_ordenada = sorted (lista, key = lambda dado: int(dado[1]), reverse = False)
    with open('Pixels_G2_ORD.csv', 'w', newline='') as file:
        for x in lista_ordenada:
            writer = csv.writer(file)
            writer.writerow([x[0],x[1]])
