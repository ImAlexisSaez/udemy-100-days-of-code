import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
SCORE_FONT = ("Arial", 16, "bold")
TEXT_FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        # Quiz
        self.quiz = quiz_brain

        # Window
        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label
        self.score_label = tk.Label(
            text=f"Score: {self.quiz.score}",
            fg="white",
            bg=THEME_COLOR,
            font=SCORE_FONT
        )
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = tk.Canvas()
        self.canvas.config(bg="white", width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="Test",
            fill="black",
            font=TEXT_FONT,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        right_img = tk.PhotoImage(file="images/true.png")
        self.right_button = tk.Button(
            image=right_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.true_pressed
        )
        self.right_button.grid(row=2, column=0)

        fail_img = tk.PhotoImage(file="images/false.png")
        self.fail_button = tk.Button(
            image=fail_img,
            highlightthickness=0,
            borderwidth=0,
            command=self.false_pressed
        )
        self.fail_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_label.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"Quiz finished\nTotal score: {self.quiz.score} / 10."
            )
            self.right_button.config(state="disabled")
            self.fail_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)


