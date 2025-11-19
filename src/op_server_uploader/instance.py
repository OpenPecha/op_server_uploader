import requests
from op_server_uploader.config import OPENPECHA_SERVER_URL


def upload_instance(text_id, instance, base_server_url):
    url = f"{base_server_url}/texts/{text_id}/instances"
    response = requests.post(url, json=instance)
    if response.status_code != 201:
        raise Exception(f"Error uploading instance: {response.text}")
    else:
        return response.json()["id"]

def upload_add_search_segmentation(instance_id, search_segmentation, base_server_url):
    url = f"{base_server_url}/annotations/{instance_id}/annotation"
    response = requests.post(url, json=search_segmentation)
    if response.status_code != 201:
        raise Exception(f"Error uploading search segmentation: {response.text}")
    else:
        return response.json()["annotation_id"]

def upload_translation_instance(source_instance_id, translation_payload, base_server_url):
    url = f"{base_server_url}/instances/{source_instance_id}/translation"
    response = requests.post(url, json=translation_payload)
    if response.status_code != 201:
        raise Exception(f"Error uploading translation instance: {response.text}")
    else:
        instance_id = response.json()["instance_id"]
        text_id = response.json()["text_id"]
        return text_id, instance_id

def upload_commentary_instance(root_instance_id, commentary_payload, base_server_url):
    url = f"{base_server_url}/instances/{root_instance_id}/translation"
    response = requests.post(url, json=commentary_payload)
    if response.status_code != 201:
        raise Exception(f"Error uploading translation instance: {response.text}")
    else:
        instance_id = response.json()["instance_id"]
        text_id = response.json()["text_id"]
        return text_id, instance_id