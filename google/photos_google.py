from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

import pickle
import requests
import os


SCOPES = [
    "https://www.googleapis.com/auth/photoslibrary.appendonly"
]


def obtener_token():
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "client_secret.json",
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return creds.token


def crear_nuevo_album(nombre_album: str) -> None:

    token = obtener_token()

    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    data = {
        "album": {
            "title": nombre_album
        }
    }

    response = requests.post(
        "https://photoslibrary.googleapis.com/v1/albums",
        headers=headers,
        json=data
    )

    response.raise_for_status()

    print("Álbum creado correctamente")

if __name__ == "__main__":
    obtener_token()
    crear_nuevo_album("test-album-1")