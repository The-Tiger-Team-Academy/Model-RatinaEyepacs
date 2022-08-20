
import tensorflow as tf
from tensorflow import keras 
from keras.models import load_model
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

new_model = load_model('Eye_Ep100.h5')
new_model.summary()
new_model.get_weights()
new_model.optimizer



testpath = 'test_opt/' 

testImg = [testpath]
rimg = []
for imagePath in (testImg):
    for item in (os.listdir(imagePath)):
        file = os.path.join(imagePath, item)
        if item.split('.')[0] != "":
          img = cv2.imread(file , cv2.COLOR_BGR2RGB)
          ori = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
          img = cv2.resize(img ,(128,128))
          rimg = np.array(img)
          rimg = rimg.astype('float32')
          rimg /= 255
          rimg = np.reshape(rimg ,(1,128,128,3))
          predict = new_model.predict(rimg)
          label = ['Normal','Dr']
          result = label[np.argmax(predict)]
          print(predict)
          print('Actual: '+str(item))   # Read actual value from filename
          print('predict: '+str(result)+' ' + str(np.round(predict.max()*100,2))+ ' %')
          predict = predict*100
          plt.imshow(ori)
          plt.show()



