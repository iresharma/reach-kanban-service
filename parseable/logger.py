from __future__ import annotations
import json
import os
import uuid
import base64
from enum import Enum

import requests

url = os.environ.get('PARSEABLE_URL')
parseable_url = f"{url}/api/v1/logstream/kanbanserver"


class LogLevel(Enum):
    INFO = "info"
    ERROR = "error"


class InfoEvent:
    def __init__(self, type: LogLevel, message: str, board: str | None, context: dict):
        self.type = type
        self.message = message
        self.board = board
        self.context = context

    def to_json(self):
        return json.dumps({
            "id": str(uuid.uuid4()),
            "type": str(self.type),
            "message": self.message,
            "X-Board": self.board,
            "context": json.dumps(self.context)
        })


class ErrorEvent:
    def __init__(self, type: LogLevel, error: Exception, board: str | None, context: dict, message: str | None = None):
        self.type = type
        self.message = message
        self.error = error
        self.board = board
        self.context = context

    def to_json(self):
        return json.dumps({
            "id": str(uuid.uuid4()),
            "type": str(self.type),
            "message": self.message if self.message else str(self.error),
            "error": str(type(self.error)),
            "X-Board": self.board,
            "context": json.dumps(self.context)
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
    res = requests.post(url=parseable_url, headers=headers, data=payload)
    print(res.status_code)


def infoLog(message: str, board: str | None=None, context: dict | None=None):
    log_event = InfoEvent(type=LogLevel.INFO, message=message, board=board, context=context)
    send_log_event(log_event)


def ErrorLog(error: Exception, board: str | None=None, context: dict | None=None, message: str | None=None):
    log_event = ErrorEvent(type=LogLevel.ERROR, message=message, board=board, context=context, error=error)
    send_log_event(log_event)
