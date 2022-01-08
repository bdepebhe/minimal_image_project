from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import base64
import numpy as np
from pydantic import BaseModel
import tensorflow as tf

class Image(BaseModel):
    image: str
    height: int
    width: int
    channel: int

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

model = tf.keras.models.load_model('saved_model/my_model')


@app.get("/")
def home():
    return {"greeting": "Welcome to the minimal image project API"}

@app.post("/predict")
def predict_class(Img: Image):
    #decode image
    decoded = base64.b64decode(bytes(Img.image, 'utf-8'))
    decoded = np.frombuffer(decoded, dtype='uint8')
    decoded = decoded.reshape(Img.height, Img.width, Img.channel)[None,:,:,:]
    #predict class
    prediction = model.predict(decoded)[0,0]
    prediction = float(prediction) # the output dtype of the network, np.float32, is not serializable in json
    return {'proba_of_class_1' : prediction}