from pathlib import Path
import numpy as np
import cv2
import insightface


DATABASE_PATH = Path.cwd().parent / "database"


class EmbeddingWriter:
    def __init__(self) -> None:
        self.embedding_base = DATABASE_PATH / "embedding_base.npy"
        self.person_base = DATABASE_PATH / "person_base.txt"

        try:
            self.embeddings = np.load(str(self.embedding_base))
        except:
            self.embeddings = np.random.randn(1, 512)
        
        try:
            with open(self.person_base, "r") as person_base_file:
                self.persons = [person_name.replace("\n", "") for person_name in person_base_file]
        except:
            self.persons = []

        self.model = insightface.app.FaceAnalysis()
        self.model.prepare(ctx_id=-1)

    def write(self, name: str) -> None:
        cap = cv2.VideoCapture(0)

        while True:
            success, image = cap.read()
            if not success:
                print("Ignoring empty camera frame.")
                continue

            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            faces = self.model.get(image_rgb)

            try:
                face = faces[0]
            except:
                continue

            embedding = face.embedding

            self.embeddings = np.concatenate([self.embeddings, embedding.reshape((1, -1))], axis=0)
            self.persons.append(name)
            break

        cap.release()
        cv2.destroyAllWindows()

    def save(self) -> None:
        with open(self.embedding_base, "wb") as embedding_base_file:
            np.save(embedding_base_file, self.embeddings)
        with open(self.person_base, "w") as person_base_file:
            for person in self.persons:
                person_base_file.write(person + "\n")


if __name__ == "__main__":
    writer = EmbeddingWriter()
    writer.write("Krzychu_v2")
    writer.save()

        
