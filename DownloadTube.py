#Escrito por: Santi Modsz
#Instagram: @pratt_santiago
#YouTube: Santi Modsz

import pytube
import sys
import os

#carpeta en que se descarga
path = input("¿donde quieres que se guarde el video?:")

#Descarga del video
url = input("Pon la url del video que quieres descargar:")
yt = pytube.YouTube(url)
yt.streams.first().download(path)
print("El video se descargó correctamente en")
print(path)
reiniciar = input("¿quieres descargar otro video? [s] [n]")
if reiniciar == "s":
 os.system('python3 descargar.py')

if reiniciar == "n":
 print("╔───────────────────────────────────────────────────────────╗")
 print("|           Autor: Santi Modsz                              |")
 print("|   Github: https://github.com/SantiModsz/DownloadTube.git  |")
 print("|   Gracias por utilizar esta herramienta                   |")
 print("|                      <3                                   |")
 print("┖───────────────────────────────────────────────────────────┙")

