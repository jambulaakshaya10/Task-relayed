import tkinter as tk
from tkinter import messagebox
import random

class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Quiz App")
        
        self.flashcards = []  # List to store flashcards as tuples (question, answer)
        self.current_flashcard_index = 0
        self.score = 0
        
        # Create GUI components
        self.create_widgets()
        
    def create_widgets(self):
        """Create the GUI elements for the application."""
        
        # Add Flashcard Section
        self.add_flashcard_frame = tk.Frame(self.root)
        self.add_flashcard_frame.pack(pady=10)

        self.question_label = tk.Label(self.add_flashcard_frame, text="Question:")
        self.question_label.grid(row=0, column=0, padx=5, pady=5)

        self.answer_label = tk.Label(self.add_flashcard_frame, text="Answer:")
        self.answer_label.grid(row=1, column=0, padx=5, pady=5)

        self.question_entry = tk.Entry(self.add_flashcard_frame, width=30)
        self.question_entry.grid(row=0, column=1, padx=5, pady=5)

        self.answer_entry = tk.Entry(self.add_flashcard_frame, width=30)
        self.answer_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_flashcard_button = tk.Button(self.add_flashcard_frame, text="Add Flashcard", command=self.add_flashcard)
        self.add_flashcard_button.grid(row=2, columnspan=2, pady=10)
        
        # Quiz Section
        self.quiz_frame = tk.Frame(self.root)
        self.quiz_frame.pack(pady=10)

        self.start_quiz_button = tk.Button(self.quiz_frame, text="Start Quiz", command=self.start_quiz)
        self.start_quiz_button.pack(pady=5)

        self.quiz_container = tk.Frame(self.root)
        self.quiz_container.pack(pady=20)
        
        self.quiz_question_label = tk.Label(self.quiz_container, text="Question", font=("Helvetica", 16))
        self.quiz_question_label.pack()

        self.user_answer_entry = tk.Entry(self.quiz_container, width=30)
        self.user_answer_entry.pack(pady=5)

        self.check_answer_button = tk.Button(self.quiz_container, text="Check Answer", command=self.check_answer)
        self.check_answer_button.pack(pady=5)
        
        self.score_label = tk.Label(self.quiz_container, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=5)
        
        self.next_button = tk.Button(self.quiz_container, text="Next", command=self.next_flashcard)
        self.next_button.pack(pady=5)
        
        self.quiz_container.pack_forget()  # Hide quiz section initially
    
    def add_flashcard(self):
        """Add a flashcard to the list."""
        question = self.question_entry.get().strip()
        answer = self.answer_entry.get().strip()

        if question and answer:
            self.flashcards.append((question, answer))
            self.question_entry.delete(0, tk.END)
            self.answer_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Flashcard added successfully!")
        else:
            messagebox.showerror("Input Error", "Both question and answer are required.")
    
    def start_quiz(self):
        """Start the quiz by showing the first flashcard."""
        if not self.flashcards:
            messagebox.showwarning("No Flashcards", "Please add some flashcards first.")
            return
        
        self.score = 0
        self.current_flashcard_index = 0
        self.score_label.config(text="Score: 0")
        self.start_quiz_button.pack_forget()  # Hide start button
        self.quiz_container.pack()  # Show quiz container
        
        self.show_flashcard()

    def show_flashcard(self):
        """Display the current flashcard's question."""
        flashcard = self.flashcards[self.current_flashcard_index]
        self.quiz_question_label.config(text=flashcard[0])
        self.user_answer_entry.delete(0, tk.END)

    def check_answer(self):
        """Check if the user's answer is correct."""
        flashcard = self.flashcards[self.current_flashcard_index]
        user_answer = self.user_answer_entry.get().strip().lower()
        
        if user_answer == flashcard[1].lower():
            self.score += 1
            messagebox.showinfo("Correct", "That's the correct answer!")
        else:
            messagebox.showerror("Incorrect", f"The correct answer was: {flashcard[1]}")

        self.score_label.config(text=f"Score: {self.score}")
        self.next_button.config(state=tk.NORMAL)

    def next_flashcard(self):
        """Move to the next flashcard."""
        self.current_flashcard_index += 1
        
        if self.current_flashcard_index >= len(self.flashcards):
            messagebox.showinfo("Quiz Complete", f"Quiz complete! Your final score is: {self.score}")
            self.quiz_container.pack_forget()
            self.start_quiz_button.pack()  # Show start button again
        else:
            self.show_flashcard()
            self.next_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = FlashcardApp(root)
    root.mainloop()

