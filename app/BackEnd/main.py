from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from enum import Enum
from pathlib import Path
from pydantic import BaseModel
import io
from PIL import Image
from models.models import ArtisRecognition

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AvailableModels(Enum):
    vgg19_001 = 'vgg19_001'
    vgg19_002 = 'vgg19_002'


models_path = Path('models')
models = {'vgg19_001': ArtisRecognition(str(models_path / 'vgg19_001')),
        "vgg19_002" : ArtisRecognition(str(models_path / 'vgg19_001'))
    }

@app.post("/{model}")
async def predict(model: AvailableModels = AvailableModels.vgg19_001, file: bytes = File(...)):
    """
    Serves predictions given an image file.

    Inputs:
        - model: name of the model being used to do the prediction
        - file: image to detect objects
    """
    model = models[model.value]
    img = Image.open(io.BytesIO(file))
    output = model.predict(img)
    return output
