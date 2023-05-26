import cv2
import insightface
import os
from typing import Protocol
import numpy as np
from backend.person_base import EmbeddingSelector


class ConnectionError(Exception):
    pass


AWS_STREAM_URL = os.getenv("AWS_STREAM_URL", None)
if not AWS_STREAM_URL:
    raise ConnectionError()


class PersonSelector(Protocol):
    threshold: float
    def compare(self, faces: np.ndarray) -> tuple[list[list[str], list[int]]]:
        pass

try:
    selector = EmbeddingSelector(threshold = 0.5)
except ValueError:
    selector = None


model = insightface.app.FaceAnalysis()

model.prepare(ctx_id=-1)

def display_streamed_video(url):
    cap = cv2.VideoCapture(url)

    while True:
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        faces = model.get(image_rgb)

        face_images = np.stack([face.embedding for face in faces])

        names, indices = selector.compare(faces=face_images) if selector else ([], [])
        for idx, face in enumerate(faces):
            if idx in indices:
                bbox = face.bbox.astype(int)
                cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
        cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    display_streamed_video(AWS_STREAM_URL)
