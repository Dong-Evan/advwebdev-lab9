# src/services/quiz_service.py
from src.models.quiz_model import QuizModel


class QuizService:
    def create_quiz(self, quiz_data):
        # Retrieve "title" and "questions" from `quiz_data` dictionary
        title = quiz_data.get('title')
        questions = quiz_data.get('questions')

        # Initialize a QuizModel with `title` and `questions`
        new_quiz = QuizModel(title, questions)

        # Call `save()` on the quiz instance and return `quiz.id`
        new_quiz.save()

        return new_quiz.id

    def get_quiz(self, quiz_id):
        # Use QuizModel's `get_quiz` method to retrieve the quiz and return it
        return QuizModel.get_quiz(quiz_id)

    def evaluate_quiz(self, quiz_id, user_answers):
        # Call `get_quiz` with `quiz_id` and store the result in `quiz`
        quiz = QuizModel.get_quiz(quiz_id)

        # If `quiz` is None, return None and "Quiz not found"
        if quiz is None:
            return None, "Quiz not found"

        # Compare `user_answers` with `quiz.questions`, count correct answers,
        # and return the score
        score = 0
        for i in range(len(user_answers)):
            if quiz.questions[i]['answer'] == user_answers[i]:
                score += 1

        return score, "Quiz evaluated successfully"
