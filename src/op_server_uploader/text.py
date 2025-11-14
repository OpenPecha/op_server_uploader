import requests
from op_server_uploader.config import OPENPECHA_SERVER_URL


def upload_text(text_metadata):
    url = f"{OPENPECHA_SERVER_URL}/texts"
    response = requests.post(url, json=text_metadata)
    if response.status_code != 201:
        raise Exception(f"Error uploading text: {response.text}")
    else:
        text_id = response.json()["id"]
        return text_id