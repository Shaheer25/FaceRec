from deepface import DeepFace

result = DeepFace.verify(img1_path ="views/img1.jpg", img2_path ="views/img2.jfif")

print(result)

models = [
  "VGG-Face",
  "Facenet",
  "Facenet512",
  "OpenFace",
  "DeepFace",
  "DeepID",
  "ArcFace",
  "Dlib",
  "SFace",
]

#face verification
result = DeepFace.verify(img1_path = "views/img1.jpg",
      img2_path = "views/img2.jpg",
      model_name = models[0]
)



#embeddings
embedding_objs = DeepFace.represent(img_path = "views/img2.jpg",
      model_name = models[2]
)