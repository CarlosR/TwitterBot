# To exectute this script you will need to install the following modules:
# pip install tensorflow pillow silence_tensorflow --user
# Nota: Tensorflow is a big A.I. library, it can take a while to install 

from silence_tensorflow import silence_tensorflow
silence_tensorflow() #This library is to prevent Tensorflow from showing alerts or debug information
import tensorflow as tf #AI Processing Library
import tensorflow.keras as kr      #AI Processing Library with examples
import numpy as np      #Numbers and arrays processing library

from tensorflow.keras.preprocessing import image #For image managing
from tensorflow.keras.applications.inception_v3 import InceptionV3, decode_predictions #Neural network model trained to recognize images

#initialization of a variable with the neural network
iv3 =  InceptionV3()


def reconocerImagen(imageFromUser):
    #changing dimension of image to 299x299 pixels
    imageRedim = image.load_img(imageFromUser, target_size=(299,299))
    
    #Creation of array, where each element is a pixel
    #each pixel is represented as an arrau of 3 numbers that range from 0 to 255
    #each element of the three numbers that represent each pixel indicate the RGB color
    x =  image.img_to_array(imageRedim)
    
    #Converting each value of 0 to 255 using the rule of 3 so that they are converted to a range of -1 to 1
    #where -1 = 0 and 1 = 255
    x /= 255
    x -= 0.5
    x *= 2
    
    #A value of 1 is added to each pixed, requested by the neural network
    x = x.reshape(1, x.shape[0], x.shape[1], x.shape[2])
    
    #the numerical matrix of pixels is sent to the neural network so that it recognizes the image
    y = iv3.predict(x)
    
    #we return the prediction along with the % of probability
    result = decode_predictions(y)[0][0]
    element = result[1]
    probability = result[2]
    return {"element":element, "probability":probability}
    
#Example code to run the function:
#prediction = recognizeImage("img1.jpg")
#print("Image detection: " + prediction["element"] + " with a probability of " + str(int(prediction["probability"]*100)) + "%" )