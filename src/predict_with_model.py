import time
import keras
import numpy as np
from keras.models import load_model
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
import tensorflow
import pandas as pd
start = time.time()
model = load_model('nnmodel.h5')

dataset = pd.read_csv('review.csv')
dataset.user_id = dataset.user_id.astype('category').cat.codes.values
dataset.business_id = dataset.business_id.astype('category').cat.codes.values
train, test = train_test_split(dataset, test_size=0.2)
n_users, n_businesses = len(dataset.user_id.unique()), len(dataset.business_id.unique())

y_pred = np.round(model.predict([test.user_id, test.business_id]),0)
y_true = test.stars
print(mean_absolute_error(y_true, y_pred))
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

# plt.figure(2)
# plt.plot(history.history['loss'])
# plt.plot(history.history['val_loss'])
# plt.title('model loss')
# plt.ylabel('loss')
# plt.xlabel('epoch')
# plt.legend(['train', 'test'], loc='upper left')
# plt.savefig('loss.png')