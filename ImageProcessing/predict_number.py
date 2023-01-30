import tensorflow as tf
import cv2
from keras.datasets import mnist
from keras.layers import Dense,Conv2D,AveragePooling2D, Flatten
from keras.models import Sequential
import numpy as np
import matplotlib.pyplot as plt

(X_train,y_train),(X_test,y_test)=mnist.load_data()
plt.imshow(X_train[0])
plt.title(y_train[0])
plt.show()

model=Sequential()
model.add(Conv2D(input_shape=(28,28,1),filters = 4, kernel_size = (5,5), activation='relu' ))
model.add(AveragePooling2D(pool_size=(2,2)))
model.add(Conv2D(input_shape=(28,28,1),filters = 4, kernel_size = (7,7) ))
model.add(AveragePooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(units=10,activation='softmax'))
model.compile(loss="sparse_categorical_crossentropy",optimizer="adam",metrics=['acc'])
model.summary()

model.fit(X_train,y_train,epochs=1,batch_size=1)

plt.imshow(X_test[10])
plt.show()
test=X_test[10].reshape(-1,28,28)
out=model.predict(test)
print(out)
classes=list(range(10))
print(classes[np.argmax(out[0])])