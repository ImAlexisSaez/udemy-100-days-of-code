import html

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = html.unescape(question["question"])  # There are special characters
    question_correct_answer = question["correct_answer"]
    question_bank.append(Question(question_text, question_correct_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score} / {quiz.question_number}.")