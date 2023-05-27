from datetime import datetime
import time
import cv2
import insightface
import os
from typing import Protocol
import numpy as np
from backend.person_base import EmbeddingSelector
from backend.alerts import send_alert


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
    selector = EmbeddingSelector(threshold = 0.4)
except ValueError:
    selector = None


model = insightface.app.FaceAnalysis()

model.prepare(ctx_id=-1)

def display_streamed_video(url):
    cap = cv2.VideoCapture(0)

    last_execution = time.time()

    while True:
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            continue

        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        faces = model.get(image_rgb)
        
        if faces:
            
            face_images = np.stack([face.embedding for face in faces])

            names, indices = selector.compare(faces=face_images) if selector else ([], [])
            face_arrays = []
            for idx, face in enumerate(faces):
                bbox = face.bbox.astype(int)
                if idx in indices:
                    cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)
                    try:
                        face_arrays.append((image[bbox[1]:bbox[3], bbox[0]:bbox[2]], names[idx]))
                        send_alert(image=image, face_image=image[bbox[1]:bbox[3], bbox[0]:bbox[2]], timestamp=datetime.now(), name=names[idx])
                    except:
                        pass
                else:
                    try:
                        blurred = cv2.blur(image[bbox[1]:bbox[3], bbox[0]:bbox[2]], (25, 25))
                        image[bbox[1]:bbox[3], bbox[0]:bbox[2]] = blurred
                    except:
                        continue
            if time.time() - last_execution > 10:
                last_execution = time.time()
                for face_img, name in face_arrays:
                    send_alert(image=image, face_image=face_img, timestamp=datetime.now(), name=name)
                    
        cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
 
if __name__ == "__main__":
    display_streamed_video(AWS_STREAM_URL)
