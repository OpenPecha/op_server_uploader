import requests


def upload_text(text_metadata, base_server_url):
    url = f"{base_server_url}/texts"
    response = requests.post(url, json=text_metadata)
    if response.status_code != 201:
        raise Exception(f"Error uploading text: {response.text}")
    else:
        text_id = response.json()["id"]
        return text_id