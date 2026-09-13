import os
import uuid
import requests

BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"


def test_create_folder():
    token = os.getenv("YANDEX_TOKEN")

    folder_name = f"test_folder_netology_{uuid.uuid4().hex}"

    headers = {
        "Authorization": f"OAuth {token}"
    }

    params = {
        "path": folder_name
    }

    response = requests.put(
        BASE_URL,
        headers=headers,
        params=params
    )

    assert response.status_code == 201


def test_create_folder_invalid_token():
    headers = {
        "Authorization": "OAuth invalid_token_12345"
    }

    params = {
        "path": "test_folder_invalid"
    }

    response = requests.put(
        BASE_URL,
        headers=headers,
        params=params
    )

    assert response.status_code == 401