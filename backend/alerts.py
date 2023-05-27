import requests
import numpy as np
import datetime
import cv2
import uuid
import base64


def send_alert(image: np.ndarray, face_image: np.ndarray, timestamp: datetime.datetime, name: str) -> None:
    _, buffer = cv2.imencode('.jpg', image)
    image_base64 = base64.b64encode(buffer).decode('utf-8')

    _, buffer = cv2.imencode('.jpg', face_image)
    face_image_base64 = base64.b64encode(buffer).decode('utf-8')

    image_data = {
        "id": f"{uuid.uuid4()}",
        "image": image_base64,
        "face_image": face_image_base64,
        "name": name,
        "timestamp": timestamp.strftime('%m/%d/%Y, %H:%M:%S')
    }

    response = requests.post("http://127.0.0.1:8000/save_images", json=image_data)


if __name__ == "__main__":
    send_alert(
        image=np.random.randint(low=0, high=255, size=(224,224,3)).astype(np.uint8),
        face_image=np.random.randint(low=0, high=255, size=(224,224,3)).astype(np.uint8),
        name="John",
        timestamp=datetime.datetime.today()
    )