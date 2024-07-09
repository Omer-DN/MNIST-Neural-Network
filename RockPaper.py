import tkinter as tk
from PIL import Image, ImageTk
import random
import os

class RockPaperNumbersGame:
    def __init__(self, root, rock_folder, paper_folder, numbers_folder):
        self.root = root
        self.root.title("Rock-Paper-Numbers Game")

        self.choices = ["rock", "paper", "numbers"]
        self.images = {
            "rock": self.load_images(rock_folder),
            "paper": self.load_images(paper_folder),
            "numbers": self.load_images(numbers_folder),
        }

        self.user_label = tk.Label(self.root, text="User's Choice:")
        self.user_label.pack()

        self.user_image_label = tk.Label(self.root)
        self.user_image_label.pack()

        self.computer_label = tk.Label(self.root, text="Computer's Choice:")
        self.computer_label.pack()

        self.computer_image_label = tk.Label(self.root)
        self.computer_image_label.pack()

        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

        self.play_again_button = tk.Button(self.root, text="Play Again", command=self.play_game)
        self.play_again_button.pack()

        self.user_wins_count = 0
        self.computer_wins_count = 0

        self.play_game()

    def load_images(self, folder):
        images = {}
        for filename in os.listdir(folder):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.jfif')):
                name = os.path.splitext(filename)[0]
                image_path = os.path.join(folder, filename)
                img = Image.open(image_path)
                # Resize 'paper' image to 100x100
                if name == "paper":
                    img = img.resize((100, 100), Image.ANTIALIAS)
                images[name] = ImageTk.PhotoImage(img)
        return images

    def get_user_choice(self):
        return random.choice(self.choices)

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie"
        elif (user_choice == "rock" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "numbers") or \
             (user_choice == "numbers" and computer_choice == "rock"):
            self.computer_wins_count += 1
            return "Computer wins"
        else:
            self.user_wins_count += 1
            return "User wins"

    def play_game(self):
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()

        self.user_image_label.config(image=self.images[user_choice][user_choice])
        self.computer_image_label.config(image=self.images[computer_choice][computer_choice])

        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=result)

        # Display results after every game
        if self.user_wins_count + self.computer_wins_count > 0:
            result_str = f"User wins: {self.user_wins_count}, Computer wins: {self.computer_wins_count}"
            tk.messagebox.showinfo("Game Results", result_str)

if __name__ == "__main__":
    root = tk.Tk()
    # Replace with your actual folder paths
    rock_folder = r"C:\Users\USER\Desktop\play\rock"
    paper_folder = r"C:\Users\USER\Desktop\play\paper"
    numbers_folder = r"C:\Users\USER\Desktop\play\numbers"
    game = RockPaperNumbersGame(root, rock_folder, paper_folder, numbers_folder)
    root.mainloop()
