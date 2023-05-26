import numpy as np
from pathlib import Path

DATABASE_PATH = Path.cwd().parent / "xebia-hackathon-flowchain/backend/database"

class PersonSelector():

    threshold: float
    database: np.ndarray

    def __init__(self, treshold: float):
        
        self.threshold = treshold
        self.database_path = DATABASE_PATH / "dummy_face_data.npy"
        self.person_base = DATABASE_PATH / "person_base.txt"

        try:
            self.database = np.load(str(self.database_path))
        except:
            raise ValueError()
        
        try:
            with open(self.person_base, "r") as person_base_file:
                self.persons = [person_name.replace("\n", "") for person_name in person_base_file]
        except:
            raise ValueError()

    def compare(self, faces: np.ndarray) -> tuple[list[list[str], list[int]]]:
        
        print(self.database.shape)
        print(faces.shape)
        print(self.persons)

        persons_indices = []
        faces_indices = []

        for face in faces:
            distances = np.dot(self.database, face.T) / (
                np.linalg.norm(self.database, axis=1) * np.linalg.norm(face)
            )

            if np.any(distances > self.threshold):
                person_idx = np.argmax(distances, axis=-1)
                
                faces_indices.append(person_idx)
                persons_indices.append(self.persons[person_idx])
        
        return faces_indices, persons_indices
        
        


if __name__ == "__main__":

    selector = PersonSelector(0.5)

    #incoming_faces = np.random.rand(3, 512)
    incoming_faces = [
        [0.1, 0.2, 0.3, 0.4, 0.5],
        [0.6, 0.7, 0.8, 0.9, 0.4],
        [0.9, 0.4, 0.5, 0.7, 0.2]
    ]

    incoming_faces = np.array(incoming_faces)
    
    print(selector.compare(incoming_faces))

    
    # Create a random 10x5 array
    

    # Print the random array
    #print(random_array)


#threshold = 0.5

# for face in x:
#     print(np.argmax(((np.dot(base, face)/(np.linalg.norm(base, axis=-1)*np.linalg.norm(face)) > threshold).astype(int)), axis=-1))



# # Create dummy data for face recognition
# face_data = [
#     [0.1, 0.2, 0.3, 0.4, 0.5],
#     [0.6, 0.7, 0.8, 0.9, 1.0],
#     [1.1, 1.2, 1.3, 1.4, 1.5]
# ]

# # Convert the data to a numpy array
# face_array = np.array(face_data)

# # Save the data array to a npy file
# np.save('face_data.npy', face_array)