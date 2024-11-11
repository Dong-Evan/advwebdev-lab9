# tests/test_quiz.py
from unittest.mock import patch, MagicMock
from src.services.quiz_service import QuizService


# Test for creating a new quiz
@patch.object(QuizService, 'create_quiz')
def test_create_quiz(mock_create_quiz, client):

    # Set `mock_create_quiz.return_value` to 1 (a mock quiz ID)
    mock_create_quiz.return_value = 1

    # Use `client.post` to send a POST request to `/api/quizzes` with JSON data
    new_quiz_data = {
        'title': 'Sample Quiz',
        'questions': []
    }
    response = client.post(
        '/api/quizzes',
        json=new_quiz_data
        )

    # Assert that status code is 201, `quiz_id` in response is 1, and
    # `mock_create_quiz` was called once
    assert response.status_code == 201
    assert response.json["quiz_id"] == 1 
    mock_create_quiz.assert_called_once()


# Test for retrieving a quiz by ID
@patch.object(QuizService, 'get_quiz')
def test_get_quiz(mock_get_quiz, client):
    # Create a MagicMock named `mock_quiz`, set `title` to "Sample Quiz",
    # and `questions` to a sample list
    mock_quiz = MagicMock(title='Sample Quiz',
                          questions=[{'text': 'q1', 'answer': 'a1'}])
    # mock_quiz = {
    #     'title': 'Sample Quiz',
    #     'questions': [
    #         {'text': 'q1', 'answer': 'a1'}]
    #         }

    # Set `mock_get_quiz.return_value` to `mock_quiz`
    mock_get_quiz.return_value = mock_quiz

    # Use `client.get` to send a GET request to `/api/quizzes/1`
    response = client.get('/api/quizzes/1')
    # print(response.json)

    # Assert that status code is 200, `title` in response is "Sample Quiz",
    # and `mock_get_quiz` was called once
    assert response.status_code == 200
    assert response.json['title'] == 'Sample Quiz'
    mock_get_quiz.assert_called_once()


# Test for submitting answers and evaluating a quiz
@patch.object(QuizService, 'evaluate_quiz')
def test_submit_quiz(mock_evaluate_quiz, client):

    # Set `mock_evaluate_quiz.return_value` to
    # (1, "Quiz evaluated successfully")
    mock_evaluate_quiz.return_value = (1, "Quiz evaluated successfully")

    # Use `client.post` to send a POST request to `/api/quizzes/1/submit`
    # with JSON data containing answers
    response = client.post(
        '/api/quizzes/1/submit',
        json={'answers': ['a1']}
    )

    # Assert that status code is 200, `score` in response is 1, `message` is
    # "Quiz evaluated successfully", and `mock_evaluate_quiz` was called once
    assert response.status_code == 200
    assert response.json['score'] == 1
    assert response.json['message'] == "Quiz evaluated successfully"
    mock_evaluate_quiz.assert_called_once()
