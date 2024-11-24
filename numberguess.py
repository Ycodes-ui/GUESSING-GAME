import random
import tkinter as tk
from tkinter import messagebox

class GameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Guessing Game")
        self.root.geometry("300x300")
        self.root.configure(bg="black")

        self.max_attempts = 5
        self.attempts = 0
        self.target = 0
        self.max_num = 0

        self.create_widgets()

    def create_widgets(self):
        self.label1 = tk.Label(self.root, text="Welcome!", font=("Helvetica", 12), fg="white", bg="black")
        self.label1.pack(pady=20)

        self.label2 = tk.Label(self.root, text="Choose difficulty.", font=("Helvetica", 10), fg="white", bg="black")
        self.label2.pack()

        self.easy_btn = tk.Button(self.root, text="Easy (1-50)", width=15, command=self.set_easy, fg="white", bg="purple", activebackground="purple", activeforeground="white")
        self.easy_btn.pack(pady=5)

        self.medium_btn = tk.Button(self.root, text="Medium (1-100)", width=15, command=self.set_medium, fg="white", bg="purple", activebackground="purple", activeforeground="white")
        self.medium_btn.pack(pady=5)

        self.hard_btn = tk.Button(self.root, text="Hard (1-200)", width=15, command=self.set_hard, fg="white", bg="purple", activebackground="purple", activeforeground="white")
        self.hard_btn.pack(pady=5)

        self.entry = tk.Entry(self.root, fg="black", bg="white")
        self.submit_btn = tk.Button(self.root, text="Submit Guess", width=15, state="disabled", command=self.check_guess, fg="white", bg="purple", activebackground="purple", activeforeground="white")

        self.attempts_label = tk.Label(self.root, text="Attempts: 0", font=("Helvetica", 10), fg="white", bg="black")
        self.attempts_label.pack(pady=5)

    def set_easy(self):
        self.set_difficulty(50)

    def set_medium(self):
        self.set_difficulty(100)

    def set_hard(self):
        self.set_difficulty(200)

    def set_difficulty(self, max_num):
        self.max_num = max_num
        self.target = random.randint(1, self.max_num)
        self.attempts = 0
        self.update_attempts()
        self.label2.config(text=f"Enter guess (1-{self.max_num}):")

        self.easy_btn.pack_forget()
        self.medium_btn.pack_forget()
        self.hard_btn.pack_forget()

        self.entry.pack(pady=10)
        self.submit_btn.config(state="normal")
        self.submit_btn.pack()

    def check_guess(self):
        guess = self.entry.get()

        if not guess.isdigit():
            messagebox.showerror("Invalid input", "Enter a valid number.", icon='error')
            self.entry.config(bg="black", fg="white")
            return

        guess = int(guess)

        if guess < 1 or guess > self.max_num:
            messagebox.showerror("Out of range", f"Enter a number between 1 and {self.max_num}.", icon='error')
            self.entry.config(bg="black", fg="white")
            return

        self.attempts += 1
        self.update_attempts()

        if guess == self.target:
            messagebox.showinfo("Correct!", f"The number was {self.target}.")
            self.reset_game()
        elif self.attempts == self.max_attempts:
            messagebox.showinfo("Game Over", f"The correct number was {self.target}.")
            self.reset_game()
        elif guess > self.target:
            messagebox.showinfo("Too High", "Try a lower number.")
        else:
            messagebox.showinfo("Too Low", "Try a higher number.")

    def update_attempts(self):
        self.attempts_label.config(text=f"Attempts: {self.attempts}/{self.max_attempts}")

    def reset_game(self):
        self.entry.pack_forget()
        self.submit_btn.pack_forget()

        self.label2.config(text="Choose difficulty.")

        self.easy_btn.pack(pady=5)
        self.medium_btn.pack(pady=5)
        self.hard_btn.pack(pady=5)

        self.update_attempts()

def main():
    root = tk.Tk()
    app = GameApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
