import pygame
import os

pygame.init()
pygame.mixer.init()

# Lista de músicas (nomes dos arquivos)
musicas = [
    "021.mp3",
    "022.mp3",
    "023.mp3"
]

indice = 0
tocando = False

def tocar_musica():
    global tocando
    pygame.mixer.music.load(musicas[indice])
    pygame.mixer.music.play()
    tocando = True
    print(f"Tocando: {musicas[indice]} 🎶")

def parar_musica():
    global tocando
    pygame.mixer.music.stop()
    tocando = False
    print("Música parada ⏹️")

def proxima():
    global indice
    indice = (indice + 1) % len(musicas)
    tocar_musica()

def anterior():
    global indice
    indice = (indice - 1) % len(musicas)
    tocar_musica()

print("""
🎧 PLAYER DE MÚSICA 🎧
P - Play
S - Stop
N - Próxima música
B - Música anterior
Q - Sair
""")

rodando = True
while rodando:
    comando = input(">> ").lower()

    if comando == "p":
        tocar_musica()
    elif comando == "s":
        parar_musica()
    elif comando == "n":
        proxima()
    elif comando == "b":
        anterior()
    elif comando == "q":
        parar_musica()
        rodando = False
    else:
        print("Comando inválido ❌")
