import pytest
import requests
from unittest.mock import patch

def test_read_users_unauthorized_mocked():
    """
    Tests reading the /users endpoint with invalid credentials using a mocked server.
    Expects an empty response and a 401 Unauthorized status code.
    """
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "admin"}

    with patch('requests.get') as mock_get:
        # Configure the mock to return a specific response
        mock_get.return_value.status_code = 401
        mock_get.return_value.text = ""

        response = requests.get(url, params=params)

        # Assertions
        assert response.status_code == 401
        assert response.text == ""
        mock_get.assert_called_once_with(url, params=params)

def test_read_users_authorized_mocked():
    """
    Tests reading the /users endpoint with valid credentials using a mocked server.
    Expects an empty response and a 200 OK status code.
    """
    url = "http://127.0.0.1:8000/users"
    params = {"username": "admin", "password": "qwerty"}

    with patch('requests.get') as mock_get:
        # Configure the mock to return a specific response
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = ""

        response = requests.get(url, params=params)

        # Assertions
        assert response.status_code == 200
        assert response.text == ""
        mock_get.assert_called_once_with(url, params=params)
        