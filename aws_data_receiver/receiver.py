import json
from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import base64
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os
import json
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://example.com",
    "https://example.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

data_path = Path.cwd() / "images"
data_path.mkdir(exist_ok=True, parents=True)
info_path = Path.cwd() / "info"
info_path.mkdir(exist_ok=True, parents=True)


class ImageData(BaseModel):
    id: str
    image: str
    face_image: str
    name: str
    timestamp: str


@app.post("/save_images")
def save_images(image_data: ImageData):

    image_path = data_path / f"{image_data.id}_image.png"
    save_base64_image(image_data.image, image_path)

    face_image_path = data_path / f"{image_data.id}_face_image.png"
    save_base64_image(image_data.face_image, face_image_path)

    try:
        with open(info_path / 'data.json', 'r') as fp:
            data = json.load(fp)
    except:
        data = {"data": []}

    data["data"].append({
        "id": image_data.id,
        "image": str(image_path),
        "face_image": str(face_image_path),
        "name": image_data.name,
        "timestamp": image_data.timestamp
    })

    with open(info_path / 'data.json', 'w') as fp:
        json.dump(data, fp)

    return {"message": "OK"}


def save_base64_image(base64_data, file_path):
    image_data = base64.b64decode(base64_data)
    with open(file_path, "wb") as f:
        f.write(image_data)



@app.get("/get_images", response_model=list[ImageData])
def get_images():
    image_folder = data_path
    info_file = info_path / "data.json"

    data = load_data_from_json(info_file)

    if not data["data"]:
        return JSONResponse(content={"message": "Brak dostępnych danych obrazków."})

    images_data = []

    for image_info in data["data"]:
        image_id = image_info["id"]

        image_path = os.path.join(image_folder, f"{image_id}_image.png")
        face_image_path = os.path.join(image_folder, f"{image_id}_face_image.png")

        if not os.path.exists(image_path) or not os.path.exists(face_image_path):
            continue

        with open(image_path, "rb") as f:
            image_data = f.read()
            image_base64 = base64.b64encode(image_data).decode("utf-8")

        with open(face_image_path, "rb") as f:
            face_image_data = f.read()
            face_image_base64 = base64.b64encode(face_image_data).decode("utf-8")

        image_info["image"] = image_base64
        image_info["face_image"] = face_image_base64

        images_data.append(ImageData(**image_info))

    if not images_data:
        return JSONResponse(content={"message": "Nie znaleziono obrazków."})

    return images_data


def load_data_from_json(file_path):
    try:
        with open(file_path, 'r') as fp:
            data = json.load(fp)
    except FileNotFoundError:
        data = {"data": []}

    return data

@app.get("/health")
def health():
    return {"status": "OK"}