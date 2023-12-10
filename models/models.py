from typing import Dict, List
import os
from fastapi.logger import logger
from config.logging import create_log
from tensorflow.keras.models import load_model as keras_load
from keras.preprocessing import *
import json
from abc import ABC, abstractmethod
import io
import time
import tensorflow as tf
from PIL import Image
import numpy as np


LOGGER = create_log('model')

class ModelStrategy(ABC):
    """
    The ModelStrategy interface declares operations common to all supported versions
    of some algorithm.

    The Model uses this interface to call the algorithm defined by Concrete ModelStrategies.

    """
    @abstractmethod
    def __init__(self, model_path: str):
        pass

    @abstractmethod
    def load_labels(self, model_path: str):
        pass

    @abstractmethod
    def load_model(self, model_path: str):
        pass

    @abstractmethod
    def predict(self, image_path: str):
        pass


class Model():

    """
    The Model defines the interface of interest to clients.
    """

    def __init__(self, strategy: ModelStrategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> ModelStrategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: ModelStrategy) -> None:
        self._strategy = strategy

    def __call__(self, image):
        result = self._strategy.predict(image)
        print(result)
        return result


class ArtisRecognition(ModelStrategy):

    def __init__(self, model_path: str):
        self.model = self.load_model(model_path)
        self.labels = self.load_labels(model_path)

    def load_model(self, model_path: str) -> tf.keras.Model:
        start_time = time.time()
        LOGGER.info('Loading model')
        detect_fn = keras_load(os.path.join(model_path, "model.h5"))
        end_time = time.time()
        elapsed_time = end_time - start_time
        LOGGER.info(elapsed_time)
        return detect_fn
    

    def load_labels(self, model_path: str):
        try:
            with open(os.path.join(model_path, "labels.json"), 'r') as file:
                data= json.load(file)
                return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print(f"An error occurred: {e}")

    
    def predict(self, img):
        img = img.resize((224, 224))
        img = image.img_to_array(img)
        img_array = np.array(img)
        img_array /= 255.
        img_array = np.expand_dims(img_array, axis=0)
        prediction = self.model.predict(img_array)
        prediction_probability = np.amax(prediction)
        prediction_idx = np.argmax(prediction)
        return {'score': prediction_probability.tolist(),
                'label': self.labels[str(prediction_idx)].replace('_', ' ')}
