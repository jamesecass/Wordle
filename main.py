from tkinter import *
from tkinter import messagebox
import fonts
import random
import words as w
import possible_anwsers as a

class wordle:
    def __init__(self):
        self.window = Tk()
        self.window.title("Wordle")
        self.icon = PhotoImage(file="logo.png")
        self.window.iconphoto(True,self.icon)


        self.GREEN = "#008000"
        self.YELLOW = "#FFFF00"
        self.GREY = "#949494"

        fonts.font()

        self.label = Label(self.window, text="Wordle",font=("Roboto Mono", 30, "bold"), bg="White")
        self.label.grid(row=0, column=0, pady=20, sticky="n")

        self.grid_frame = Frame(self.window, bg="white")
        self.grid_frame.grid(row=3, column=0, pady=20)

        self.entry = Entry(self.window, font=("Roboto Mono", 30, "bold"))
        self.entry.grid(row=999, column=0, pady=20)
        self.entry.bind("<Return>", lambda event: self.user_input())
        self.words = w.words
        self.guessnum = 1
        self.word = random.choice(a.words)

    def generate_word(self): 
        return random.choice(self.words)

    def user_input(self):
        guess = self.entry.get().lower()
        if guess not in self.words:
            messagebox.showerror("Invalid word", "Word not recognized. Try again.")
            return
        self.entry.delete(0, END)

        if self.guessnum <= 5:
            if len(guess) == 5:
                self.guessnum += 1
                for i, letter in enumerate(guess):
                    if self.word == guess:
                        for x, g_letter in enumerate(guess):
                            lbl = Label(self.grid_frame, text=g_letter.upper(), font=("Roboto Mono", 25, "bold"), width=2)
                            lbl.grid(row=self.guessnum, column=x, padx=10, pady=10)
                            lbl.config(bg=self.GREEN)
                    else:
                        lbl = Label(self.grid_frame, text=letter.upper(), font=("Roboto Mono", 25, "bold"), width=2)
                        lbl.grid(row=self.guessnum, column=i, padx=10, pady=10)
                        if letter == self.word[i]:
                            lbl.config(bg=self.GREEN)
                        elif letter in self.word:
                            lbl.config(bg=self.YELLOW)
                        else:
                                lbl.config(bg=self.GREY)
                if self.word == guess:
                    messagebox.showinfo("Correct", f"Correct! The word was {self.word}")
                    exit()

            else:
                messagebox.showerror("Length error", "Please use a 5-letter word.")
        else:
            messagebox.showerror("Fail", f"You lost! The word was {self.word}")

    def main(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = wordle()
    app.main()
