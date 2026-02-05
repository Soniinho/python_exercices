# Matheus Henrique Daltroso RA: 202110059

from tkinter import *
import pygame  # py -m pip install pygame

root = Tk()
root.title("Player de Músicas")

root.geometry("390x370")

# Define a cor de fundo da janela do Tkinter (em hexadecimal ou por nome)
cor_de_fundo_tkinter = "#E2E2E2"
root.configure(bg=cor_de_fundo_tkinter)

pygame.mixer.init()  # inicialize o pygame

# Lista de músicas
musicas = ["Pigstep3D.mp3", "MegaTheme.mp3"]
musica_atual = 0  # Índice da música atual
pygame.mixer.music.load(musicas[0])  # load ao abrir a aplicação


def toggle_play():
    global musica_atual
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    musica_atual = (musica_atual + 1) % len(musicas)
    pygame.mixer.music.load(musicas[musica_atual])
    musica_selecionada_label.config(text=f"Música Selecionada: {musicas[musica_atual]}")


def play():
    pygame.mixer.music.play(loops=0)


musica_pausada = False

def pause_resume():
    global posicao_da_musica, musica_pausada

    if musica_pausada:
        # Retome a música da posição registrada
        pygame.mixer.music.unpause()
        musica_pausada = False
    else:
        # Pausa a música e armazena a posição atual
        posicao_da_musica = pygame.mixer.music.get_pos()
        pygame.mixer.music.pause()
        musica_pausada = True


title = Label(
    root,
    text="Música",
    font=("times new roman", 50, "bold"),
    bg=cor_de_fundo_tkinter,
    fg="black",
)
title.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

largura_label = 30
musica_selecionada_label = Label(
    root,
    text=f"Música Selecionada: {musicas[musica_atual]}",
    font=("Helvetica", 16),
    bg=cor_de_fundo_tkinter,
    width=largura_label,
)
musica_selecionada_label.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

botao_play_pause_fonte = ("Helvetica", 30)

play_toggle_button = Button(
    root, text="Alternar Música", font=("Helvetica", 24), command=toggle_play, width=15
)
play_button = Button(root, text="▶", font=botao_play_pause_fonte, command=play, width=5)
pause_button = Button(
    root, text="⏸", font=botao_play_pause_fonte, command=pause_resume, width=5
)

play_toggle_button.grid(row=2, column=0, columnspan=2, pady=10, padx=10)
play_button.grid(row=3, column=0, pady=10, padx=2)
pause_button.grid(row=3, column=1, pady=10, padx=2)

root.mainloop()
