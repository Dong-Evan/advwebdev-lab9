# src/controllers/quiz_controller.py
from flask import Blueprint, request, jsonify
from src.services.quiz_service import QuizService

quiz_bp = Blueprint('quiz', __name__, url_prefix='/api/quizzes')

@quiz_bp.route('', methods=['POST'])
def create_quiz():
    # Initialize an instance of QuizService 
    quizService = QuizService()
    
    # Get JSON data from the request using request.json and assign it to `data`
    quiz_data = request.json
    
    # Use the service to create a quiz with the `data` and store the returned quiz ID in `quiz_id`
    if quiz_data.get('title') is None or quiz_data.get('questions') is None:
        return jsonify({'error': 'no title or questions'}), 400
    quiz_id = quizService.create_quiz(quiz_data)
    
    # Use jsonify to create a JSON response containing `message` and `quiz_id`, with status code 201
    return jsonify({'message': 'Quiz created successfully', 'quiz_id': quiz_id}), 201

@quiz_bp.route('/<int:quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    # Initialize an instance of QuizService 
    quizService = QuizService()
    
    # Call the `get_quiz` method with `quiz_id` and store the result in `quiz`
    quiz = quizService.get_quiz(quiz_id)
    
    # If `quiz` exists, return it as a JSON response with status 200. Otherwise, return an error message with status 404.
    if quiz is None:
        return jsonify({'error': 'Quiz not found'}), 404
    
    return jsonify({
        'title': quiz.title,
        'questions': quiz.questions
        }), 200

@quiz_bp.route('/<int:quiz_id>/submit', methods=['POST'])
def submit_quiz(quiz_id):
    # Initialize an instance of QuizService 
    quizService = QuizService()
    
    # Get the answers from the request using `request.json.get('answers')` and store in `user_answers`
    user_answers = request.json.get('answers')
    
    # Call `evaluate_quiz` with `quiz_id` and `user_answers` and store the result in `score` and `message`
    score, message = quizService.evaluate_quiz(quiz_id, user_answers)
    
    # If `score` is None, return an error with status 404. Otherwise, return `score` and `message` with status 200.
    if score is None:
        return jsonify({'error': 'no score'}), 404
    else:
        return jsonify({'score': score, 'message': message}), 200
