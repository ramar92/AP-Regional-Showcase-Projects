from tensorflow import keras
from tensorflow.keras.layers import Input, Conv2D, MaxPooling2D, Concatenate, Conv2DTranspose, BatchNormalization, Activation
from tensorflow.keras import Model

def unet(image_height, image_width, num_classes, chan):
    # inputs = Input(input_size)
    inputs = Input(shape=(image_height, image_width, chan))
    conv1 = Conv2D(32, (3, 3), activation=None, padding='same')(inputs)
    conv1 = Activation('relu')(conv1)    
    conv1  = BatchNormalization()(conv1)
    conv1 = Conv2D(32, (3, 3), activation=None, padding='same')(conv1)
    conv1 = Activation('relu')(conv1)    
    conv1  = BatchNormalization()(conv1)
    pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
    conv2 = Conv2D(64, (3, 3), activation=None, padding='same')(pool1)
    conv2 = Activation('relu')(conv2)    
    conv2  = BatchNormalization()(conv2)
    conv2 = Conv2D(64, (3, 3), activation=None, padding='same')(conv2)
    conv2 = Activation('relu')(conv2)    
    conv2  = BatchNormalization()(conv2)
    pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
    conv3 = Conv2D(128, (3, 3), activation=None, padding='same')(pool2)
    conv3 = Activation('relu')(conv3)    
    conv3  = BatchNormalization()(conv3)
    conv3 = Conv2D(128, (3, 3), activation=None, padding='same')(conv3)
    conv3 = Activation('relu')(conv3)    
    conv3  = BatchNormalization()(conv3)
    pool3 = MaxPooling2D(pool_size=(2, 2))(conv3)
    conv4 = Conv2D(256, (3, 3), activation=None, padding='same')(pool3)
    conv4 = Activation('relu')(conv4)    
    conv4  = BatchNormalization()(conv4)
    conv4 = Conv2D(256, (3, 3), activation=None, padding='same')(conv4)
    conv4 = Activation('relu')(conv4)    
    conv4  = BatchNormalization()(conv4)
    pool4 = MaxPooling2D(pool_size=(2, 2))(conv4)
    conv5 = Conv2D(512, (3, 3), activation=None, padding='same')(pool4)
    conv5 = Activation('relu')(conv5)    
    conv5  = BatchNormalization()(conv5)
    conv5 = Conv2D(512, (3, 3), activation=None, padding='same')(conv5)
    conv5 = Activation('relu')(conv5)    
    conv5  = BatchNormalization()(conv5)
    up6 = Concatenate()([Conv2DTranspose(256, (2, 2), strides=(2, 2), padding='same')(conv5), conv4])
    conv6 = Conv2D(256, (3, 3), activation=None, padding='same')(up6)
    conv6 = Activation('relu')(conv6)    
    conv6  = BatchNormalization()(conv6)
    conv6 = Conv2D(256, (3, 3), activation=None, padding='same')(conv6)
    conv6 = Activation('relu')(conv6)    
    conv6  = BatchNormalization()(conv6)
    up7 = Concatenate()([Conv2DTranspose(128, (2, 2), strides=(2, 2), padding='same')(conv6), conv3])
    conv7 = Conv2D(128, (3, 3), activation=None, padding='same')(up7)
    conv7 = Activation('relu')(conv7)    
    conv7  = BatchNormalization()(conv7)
    conv7 = Conv2D(128, (3, 3), activation=None, padding='same')(conv7)
    conv7 = Activation('relu')(conv7)    
    conv7  = BatchNormalization()(conv7)
    up8 = Concatenate()([Conv2DTranspose(64, (2, 2), strides=(2, 2), padding='same')(conv7), conv2])
    conv8 = Conv2D(64, (3, 3), activation=None, padding='same')(up8)
    conv8 = Activation('relu')(conv8)    
    conv8  = BatchNormalization()(conv8)
    conv8 = Conv2D(64, (3, 3), activation=None, padding='same')(conv8)
    conv8 = Activation('relu')(conv8)    
    conv8  = BatchNormalization()(conv8)
    up9 = Concatenate()([Conv2DTranspose(32, (2, 2), strides=(2, 2), padding='same')(conv8), conv1])
    conv9 = Conv2D(32, (3, 3), activation=None, padding='same')(up9)
    conv9 = Activation('relu')(conv9)    
    conv9  = BatchNormalization()(conv9)
    conv9 = Conv2D(32, (3, 3), activation=None, padding='same')(conv9)
    conv9 = Activation('relu')(conv9)    
    conv9  = BatchNormalization()(conv9)
    # outputs = Conv2D(num_classes, (1, 1), activation='softmax')(conv9)
    # outputs = Conv2D(num_classes, (1, 1), activation='relu')(conv9)
    outputs = Conv2D(num_classes, (1, 1), strides=(1, 1), activation='sigmoid')(conv9)
    # outputs = Conv2D(num_classes, (1, 1), activation=None)(conv9)

    return Model(inputs=[inputs], outputs=[outputs])