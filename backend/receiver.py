import cv2
import insightface
import os


class ConnectionError(Exception):
    pass


AWS_STREAM_URL = os.getenv("AWS_STREAM_URL", None)
if not AWS_STREAM_URL:
    raise ConnectionError()


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

        for face in faces:
            bbox = face.bbox.astype(int)
            cv2.rectangle(image, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 2)

        cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    display_streamed_video(AWS_STREAM_URL)
