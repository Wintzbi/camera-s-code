import tensorflow as tf
import numpy as np
import cv2
from keras.models import load_model

model = tf.keras.applications.MobileNetV2(weights='imagenet')

image = cv2.imread('test.jpg')

resized = cv2.resize(image,(224,224))
resized = tf.keras.preprocessing.image.img_to_array(resized)
resized = tf.keras.applications.mobilenet_v2.preprocess_input(resized)

predictions = model.predict(np.array([resized]))
decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions,top=5)

for _,label,score in decoded_predictions[0]:
	print(f"Ceci est {label}: probabilité {score}")
