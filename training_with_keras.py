import pandas as pd
import numpy as np 
import tensorflow as tf
from sklearn.model_selection import train_test_split
import keras
# from IPython.display import SVG
from keras.optimizers import Adam
from sklearn.metrics import mean_absolute_error
from keras.layers import Embedding, Input, Dense, merge, Reshape, Flatten, Dropout
from keras.models import Sequential, Model, load_model, save_model
import matplotlib.pyplot as plt
# from tensorflow.python.client import device_lib
# from keras import backend as K
import time

# print(device_lib.list_local_devices())

# print (K.tensorflow_backend._get_available_gpus())

dataset = pd.read_csv('review.csv')
dataset.user_id = dataset.user_id.astype('category').cat.codes.values
dataset.business_id = dataset.business_id.astype('category').cat.codes.values
train, test = train_test_split(dataset, test_size=0.2)

n_users, n_businesses = len(dataset.user_id.unique()), len(dataset.business_id.unique())

#Matrix Factorization
# n_latent_factor = 3
# business_input = keras.layers.Input(shape=[1],name='Business')
# business_embedding = keras.layers.Embedding(n_businesses + 1, n_latent_factor, name='Business-Embedding')(business_input)
# business_vec = keras.layers.Flatten(name='FlattenBusinesses')(business_embedding)

# user_input = keras.layers.Input(shape=[1],name='User')
# user_vec = keras.layers.Flatten(name='FlattenUsers')(keras.layers.Embedding(n_users + 1, n_latent_factor,name='User-Embedding')(user_input))

# prod = keras.layers.dot([business_vec, user_vec], axes=1)

# model = Model([user_input, business_input], prod)
# model.compile('adam', 'mean_squared_error')
# history = model.fit([train.user_id, train.business_id], train.stars, epochs=100, verbose=0)
# y_hat = np.round(model.predict([test.user_id, test.business_id]),0)
# y_true = test.stars
# print (mean_absolute_error(y_true, y_hat))
# print (len(unique_users.keys()))
# print (len(dataset.user_id.unique()), len(dataset.business_id.unique()))


#NN
start = time.time()
n_latent_factors_user = 5
n_latent_factors_business = 8

business_input = keras.layers.Input(shape=[1],name='Item')
business_embedding = keras.layers.Embedding(n_businesses + 1, n_latent_factors_business, name='business-Embedding')(business_input)
business_vec = keras.layers.Flatten(name='FlattenBusinesses')(business_embedding)
business_vec = keras.layers.Dropout(0.2)(business_vec)


user_input = keras.layers.Input(shape=[1],name='User')
user_vec = keras.layers.Flatten(name='FlattenUsers')(keras.layers.Embedding(n_users + 1, n_latent_factors_user,name='User-Embedding')(user_input))
user_vec = keras.layers.Dropout(0.2)(user_vec)


concat = keras.layers.concatenate([business_vec, user_vec], axis=-1)
concat_dropout = keras.layers.Dropout(0.2)(concat)
dense = keras.layers.Dense(200,name='FullyConnected')(concat)
dropout_1 = keras.layers.Dropout(0.2,name='Dropout')(dense)
dense_2 = keras.layers.Dense(100,name='FullyConnected-1')(concat)
dropout_2 = keras.layers.Dropout(0.2,name='Dropout')(dense_2)
dense_3 = keras.layers.Dense(50,name='FullyConnected-2')(dense_2)
dropout_3 = keras.layers.Dropout(0.2,name='Dropout')(dense_3)
dense_4 = keras.layers.Dense(20,name='FullyConnected-3', activation='relu')(dense_3)


result = keras.layers.Dense(1, activation='relu',name='Activation')(dense_4)
adam = Adam(lr=0.005)
model = keras.Model([user_input, business_input], result)
model.compile(optimizer=adam,loss= 'mean_absolute_error')


history = model.fit([train.user_id, train.business_id],  train.stars, validation_split=0.33, epochs=250, verbose=0)
y_hat_2 = np.round(model.predict([test.user_id, test.business_id]),0)
y_true = test.stars
print ("=========================================")
print(mean_absolute_error(y_true, y_hat_2))
print(mean_absolute_error(y_true, model.predict([test.user_id, test.business_id])))
model.save('nnmodel.h5')

end = time.time()
print ("Finished after {} mins and {} seconds".format(int((end - start)/60), int((end - start) % 60)))
print(history.history.keys())
# plt.figure(1)
# plt.plot(history.history['acc'])
# plt.plot(history.history['val_acc'])
# plt.title('model accuracy')
# plt.ylabel('accuracy')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.savefig('training_testing_acc.png')

plt.figure(1)
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.savefig('loss.png')