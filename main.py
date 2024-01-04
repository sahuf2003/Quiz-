from data import question_data
from Question_model import Question
from Quiz_brain import QuizBrain

question_bank =[]
for mcq in question_data:
    question = Question(mcq["question"],mcq["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was{quiz.score}/{quiz.question_number}")
