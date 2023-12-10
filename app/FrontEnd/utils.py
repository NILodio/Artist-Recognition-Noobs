import requests
from io import BytesIO

def make_predictions(_image, model_choice):
    model = {'VGG19': 'vgg19_001',
             'ResNet50': 'vgg19_001'}

    file = BytesIO()
    _image.save(file, "jpeg")
    file.seek(0)
    files = {"file": ("img.jpg",
                      file,
                      'multipart/form-data',
                      {'Expires': '0'})}
    res = requests.post(f"http://fastapi:80/{model[model_choice]}",
                        files=files)
    return res.json()