import requests
from op_server_uploader.config import OPENPECHA_SERVER_URL


def upload_instance(text_id, instance):
    url = f"{OPENPECHA_SERVER_URL}/texts/{text_id}/instances"
    response = requests.post(url, json=instance)
    if response.status_code != 201:
        raise Exception(f"Error uploading instance: {response.text}")
    else:
        return response.json()["id"]

def upload_add_search_segmentation(instance_id, search_segmentation):
    url = f"{OPENPECHA_SERVER_URL}/annotations/{instance_id}/annotation"
    response = requests.post(url, json=search_segmentation)
    if response.status_code != 201:
        raise Exception(f"Error uploading search segmentation: {response.text}")
    else:
        return response.json()["annotation_id"]

def upload_translation_instance(source_instance_id, translation_payload ):
    url = f"{OPENPECHA_SERVER_URL}/instances/{source_instance_id}/translation"
    response = requests.post(url, json=translation_payload)
    if response.status_code != 201:
        raise Exception(f"Error uploading translation instance: {response.text}")
    else:
        instance_id = response.json()["instance_id"]
        text_id = response.json()["text_id"]
        return text_id, instance_id