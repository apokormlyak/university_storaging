import pytest
from rest_framework.test import APIClient
from unittest.mock import MagicMock

@pytest.fixture
def user():
    return MagicMock()

@pytest.fixture
def authenticated_client(user):
    client = APIClient()
    client.force_authenticate(user)
    return client
