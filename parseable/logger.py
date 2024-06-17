from __future__ import annotations
import json
import os
import uuid
import base64

import requests

url = os.environ.get('PARSEABLE_URL')
parseable_url = f"https://{url}/api/v1/logstream/kanbanserver"


class InfoEvent:
    def __init__(self, type: str, message: str):
        self.type = type
        self.message = message

    def to_json(self):
        return json.dumps({
            "id": str(uuid.uuid4()),
            "type": self.type,
            "message": self.message
        })


class ErrorEvent:
    def __init__(self, type: str, error: Exception, message: str | None = None):
        self.type = type
        self.message = message
        self.error = error

    def to_json(self):
        return json.dumps({
            "id": str(uuid.uuid4()),
            "type": self.type,
            "message": self.message if self.message else str(self.error),
            "error": str(type(self.error))
        })


def send_log_event(event: InfoEvent | ErrorEvent):
    credentials = os.environ.get("PARSEABLE_CREDS")
    encoded_credentials = base64.b64encode(credentials.encode("utf-8")).decode("utf-8")

    headers = {
        "Authorization": f"Basic {encoded_credentials}",
        "Content-Type": "application/json",
        "X-P-TAG-Language": "python",
    }

    payload = event.to_json()

    requests.post(url=parseable_url, headers=headers, data=payload)
