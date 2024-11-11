# src/models/quiz_model.py
from src.database import db


# Create a class named QuizModel that inherits from db.Model
class QuizModel(db.Model):
    # Define `__tablename__` as 'quizzes'
    __tablename__ = 'quizzes'

    # Define an integer primary key column named `id`
    # Define a string column named `title` that cannot be null
    # Define a column named `questions` with PickleType to store a list
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    questions = db.Column(db.PickleType)

    def __init__(self, title, questions):

        # Assign `self.title` and `self.questions` with `title` and
        # `questions`
        self.title = title
        self.questions = questions

    def save(self):

        # Use `db.session.add(self)` and `db.session.commit()` to save the
        # instance
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_quiz(cls, quiz_id):

        #  Use `cls.query.get(quiz_id)` to retrieve a quiz and return it
        return cls.query.get(quiz_id)
