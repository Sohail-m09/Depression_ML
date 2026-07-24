'''import requests

API_URL = "http://127.0.0.1:8000/predict"


def predict_depression(data):

    try:

        response = requests.post(
            API_URL,
            json=data,
            timeout=30
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:

        return {
            "error": str(e)
        }'''

import requests

API_URL = "http://127.0.0.1:8000/predict"

def predict_depression(data):

    print("\n====================")
    print("JSON SENT TO FASTAPI")
    print(data)
    print("====================\n")

    response = requests.post(API_URL, json=data)

    print("Status Code:", response.status_code)
    print("Response Text:", response.text)

    if response.status_code == 200:
        return response.json()

    return {
        "error": response.text
    }