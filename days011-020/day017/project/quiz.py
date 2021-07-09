from data import question_data, question_data_api
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []

choice = input("Do you wish to get data from API? ").lower()
if choice == 'yes':
    for question in question_data_api:
        question_bank.append(Question(question['question'], question['correct_answer']))
else:
    for question in question_data:
        question_bank.append(Question(question['text'], question['answer']))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
