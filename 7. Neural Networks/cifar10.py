'''Train a simple deep CNN on the CIFAR10 small images dataset.
'''

from __future__ import print_function
from keras.datasets import cifar10
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.utils import np_utils
import keras

batch_size = 128
nb_classes = 10
nb_epoch = 5
data_augmentation = True

# input image dimensions
img_rows, img_cols = 32, 32

# the CIFAR10 images are RGB
img_channels = 3

# the data, shuffled and split between train and test sets
(X_train, y_train), (X_test, y_test) = cifar10.load_data()
print('X_train shape:', X_train.shape)
print(X_train.shape[0], 'train samples')
print(X_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
Y_train = np_utils.to_categorical(y_train, nb_classes)
Y_test = np_utils.to_categorical(y_test, nb_classes)

model = Sequential()

# convolutional layers
model.add(Conv2D(16, (3, 3), input_shape=(img_rows, img_cols, img_channels), padding='same'))
model.add(Activation('relu'))

model.add(Conv2D(16, (3, 3)))
model.add(Activation('relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))

# convert image to vector
model.add(Flatten())

# fully connected layers
model.add(Dense(128))
model.add(Activation('relu'))

model.add(Dense(128))
model.add(Activation('relu'))

# output of the network
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

# model trained with Adam optimization procedure
model.compile(loss='categorical_crossentropy',
              optimizer=keras.optimizers.Adam(lr=0.001, beta_1=0.9, beta_2=0.999, epsilon=1e-08),
              metrics=['accuracy'])

# standardise inputs
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

# Print summary
print(model.summary())

# train the model
model.fit(X_train, Y_train,
      batch_size=batch_size,
      epochs=nb_epoch,
      validation_data=(X_test, Y_test),
      shuffle=True)

