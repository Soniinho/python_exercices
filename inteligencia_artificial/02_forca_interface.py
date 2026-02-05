import tkinter as tk
from tkinter import messagebox
import random

# Lista de palavras para o jogo
word_list = ['PYTHON', 'JAVA', 'INTERFACE', 'PROGRAMMING', 'DEVELOPER', 'SOFTWARE']

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")
        self.word = random.choice(word_list)
        self.guessed_letters = set()
        self.wrong_attempts = 0
        self.max_attempts = 6

        self.create_widgets()
        self.update_display()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.word_display = tk.Label(self.root, text='', font=('Helvetica', 20))
        self.word_display.pack()

        self.entry = tk.Entry(self.root, font=('Helvetica', 20))
        self.entry.pack()
        self.entry.bind('<Return>', self.check_letter)

        self.message_label = tk.Label(self.root, text='', font=('Helvetica', 12))
        self.message_label.pack()

        self.reset_button = tk.Button(self.root, text="Reiniciar Jogo", command=self.reset_game)
        self.reset_button.pack()

    def draw_hangman(self):
        self.canvas.delete("all")
        # Desenhando a forca fixa
        self.canvas.create_line(100, 350, 300, 350, width=5)  # Base
        self.canvas.create_line(200, 350, 200, 50, width=5)   # Poste
        self.canvas.create_line(200, 50, 300, 50, width=5)    # Braço
        self.canvas.create_line(300, 50, 300, 100, width=5)   # Corda

        # Desenhando as partes do corpo conforme as tentativas erradas
        if self.wrong_attempts > 0:
            self.canvas.create_oval(275, 100, 325, 150, width=5)  # Cabeça
        if self.wrong_attempts > 1:
            self.canvas.create_line(300, 150, 300, 250, width=5)  # Tronco
        if self.wrong_attempts > 2:
            self.canvas.create_line(300, 170, 250, 220, width=5)  # Braço esquerdo
        if self.wrong_attempts > 3:
            self.canvas.create_line(300, 170, 350, 220, width=5)  # Braço direito
        if self.wrong_attempts > 4:
            self.canvas.create_line(300, 250, 250, 300, width=5)  # Perna esquerda
        if self.wrong_attempts > 5:
            self.canvas.create_line(300, 250, 350, 300, width=5)  # Perna direita

    def update_display(self):
        display_word = ' '.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        self.word_display.config(text=display_word)

        if '_' not in display_word:
            messagebox.showinfo("Jogo da Forca", "Parabéns! Você ganhou!")
            self.reset_game()
        elif self.wrong_attempts >= self.max_attempts:
            self.draw_hangman()  # Assegura que a perna direita seja desenhada
            messagebox.showinfo("Jogo da Forca", f"Você perdeu! A palavra era {self.word}")
            self.reset_game()

        self.draw_hangman()

    def check_letter(self, event):
        letter = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if letter in self.guessed_letters:
            self.message_label.config(text="Você já tentou essa letra!")
        elif letter in self.word:
            self.guessed_letters.add(letter)
            self.message_label.config(text="Boa! Letra correta!")
        else:
            self.wrong_attempts += 1
            self.message_label.config(text="Letra errada!")

        self.update_display()

    def reset_game(self):
        self.word = random.choice(word_list)
        self.guessed_letters = set()
        self.wrong_attempts = 0
        self.update_display()
        self.message_label.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
