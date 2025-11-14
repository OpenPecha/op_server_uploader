from op_server_uploader.text import upload_text
from op_server_uploader.instance import upload_instance, upload_add_search_segmentation, upload_translation_instance

text_metadata = {
  "type": "root",
  "title": {
    "bo": "བཟོད་པ་བསྟན་པ།"
  },
  "language": "bo",
  "contributions": [
    {
      "person_bdrc_id": "P4954",
      "role": "author"
    }
  ],
  "date": "2024-01-01",
  "bdrc": "",
  "category_id": "7fVHXmQDx2Gl5nx2FdIUp",
  "copyright": "Public domain",
  "license": "CC0"
}

text_id = upload_text(text_metadata)