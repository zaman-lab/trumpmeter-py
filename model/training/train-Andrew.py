#!/usr/bin/env python
# coding: utf-8
# In[257]:
import os
from keras.preprocessing import sequence
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Embedding, SpatialDropout1D, Flatten
from keras.layers import Input
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.merge import concatenate
import numpy as np
from helper_data_formatting import get_xy
#from keras.utils.vis_utils import plot_model
from keras.models import Model
import h5py
from gensim.corpora import Dictionary

# In[257]:
########set working directory 
##os.chdir("../training/")


preprocessed=True
if not preprocessed:
  ################################################################################################
  ################################ Preprocessing #################################################
  ################################################################################################
  
  n_tweets = 550000 * 2 #for example 
  X, X_s, Y, dictionary_size, dictionary_size_s, seq_len = get_xy(n_tweets)
  
  #np.load(outfile)  
  # ## CNN
  
  # In[257]:
  #####################check X nature########
  check_dict = dict()
  
  for i in range(len(X)):
  	if str(X[i]) not in check_dict.keys():
  		check_dict[str(X[i])] = []
  		check_dict[str(X[i])].append(Y[i])
  	else:
  		check_dict[str(X[i])].append(Y[i])
  
  ab_dict = dict()
  for ele in check_dict.keys():
  	if len(set(check_dict[ele])) > 1:
  		ab_dict[ele] = check_dict[ele] 
  
  
  ################################################################################################
  ################################ METHOD 2 ######################################################
  ################################################################################################
  
  
  
  
  X_unique,indices=np.unique(X,return_index=True,axis=0)
  Y_unique = Y[indices]
  X_s_unique=X_s[indices]
  
  seed = np.random.random(X_unique.shape[0])
  
  np.random.seed(1)
  np.random.shuffle(X_unique)
  np.random.seed(1)
  np.random.shuffle(Y_unique)
  np.random.seed(1)
  np.random.shuffle(X_s_unique)
  
  
  #train dataset 80% - 20% 
  
  split = int(X_unique.shape[0]*0.8)
  
  train_X = X_unique[:split,:]
  train_Y = Y_unique[:split,]
  
  test_X = X_unique[split:,:]
  test_Y = Y_unique[split:,]
  
  #to be added to the LSTM, we need to change y to specific format 
  
  train_Y = np_utils.to_categorical(train_Y, 2)
  #test_Y = np_utils.to_categorical(test_Y, 2)
  
  #train dataset 80% - 20% 
  split = int(X_s_unique.shape[0]*0.8)
  train_X_s = X_s_unique[:split,:]
  test_X_s = X_s_unique[split:,:]
  
  np.save("train_X_s.npy",train_X_s)
  np.save("train_X.npy",train_X)
  np.save("train_Y.npy",train_Y)
  
  np.save("test_X_s.npy",test_X_s)
  np.save("test_X.npy",test_X)
  np.save("test_Y.npy",test_Y)
  
  print(train_X_s.shape,train_X.shape,train_Y.shape, test_X_s.shape, test_X.shape,test_Y.shape)
else:
  train_X_s = np.load("train_X_s.npy")
  train_X=np.load("train_X.npy")
  train_Y=np.load("train_Y.npy")
  
  test_X_s = np.load("test_X_s.npy")
  test_X=np.load("test_X.npy")
  test_Y=np.load("test_Y.npy")
  dictionary = Dictionary.load('Dictionary/dic.txt')
  dictionary_s = Dictionary.load('Dictionary/dic_s.txt')
  dictionary_size=len(dictionary)
  dictionary_size_s=len(dictionary_s)
  
  print(train_X_s.shape,train_X.shape,train_Y.shape, test_X_s.shape, test_X.shape,test_Y.shape)
# In[270]:

seq_len = train_X.shape[1]
#earlystopping
es = EarlyStopping(monitor='val_loss',
                              min_delta=0,
                              patience=3,
                              verbose=0, mode='auto')
outputFolder = './model-checkpoint'
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)
filepath=outputFolder+ "/weights-improvement-{epoch:02d}-{val_acc:.2f}.hdf5"
save = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
#input1
inputs1 = Input(shape=(seq_len,))
embedding1 = Embedding(dictionary_size + 1, 64)(inputs1)
conv1 = Conv1D(filters=32, kernel_size=3, activation='relu', padding='valid')(embedding1)
drop1 = Dropout(0.2)(conv1)
pool1 = MaxPooling1D(pool_size=2)(drop1)
flat1 = Flatten()(pool1)
#Input2
inputs2 = Input(shape=(seq_len,))
embedding2 = Embedding(dictionary_size_s + 1, 64)(inputs2)
conv2 = Conv1D(filters=32, kernel_size=3, activation='relu', padding='valid')(embedding2)
drop2 = Dropout(0.2)(conv2)
pool2 = MaxPooling1D(pool_size=2)(drop2)
flat2 = Flatten()(pool2)
#merge
merged = concatenate([flat1, flat2])
#dense
dense1 = Dense(64, activation='relu')(merged)
dense2 = Dense(32, activation='relu')(dense1)
outputs = Dense(2, activation='softmax')(dense2)

model = Model(inputs=[inputs1, inputs2], outputs=outputs)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

print(model.summary())
print(train_X_s.shape,train_X.shape,train_Y.shape, test_X_s.shape, test_X.shape,test_Y.shape)

#plot_model(model, show_shapes=True, to_file='multichannel.png')
model.fit([train_X, train_X_s], train_Y, epochs=20, batch_size=256, callbacks=[es, save], 
    validation_split=0.2)

#model.save_weights("Final_weights/final_weights.hdf5")
model.save("Final_weights/final_model.h5")
# ## Testing

# In[271]:


print('testing ...')
test_pred = model.predict([test_X, test_X_s])
test_pred = (test_pred[:,0] <= 0.5).astype(int)


score = model.evaluate( [test_X, test_X_s] , np_utils.to_categorical(test_Y, 2))
print('Test loss:', score[0])
print('Test accuracy:', score[1])


# ## Performance

# In[272]:


print("test set accuracy: ", float(sum(test_Y == test_pred)) / test_Y.shape[0])


print("base line accuracy: ", max(sum(train_Y[:,1])/len(train_Y[:,1]),1 - sum(train_Y[:,1])/len(train_Y[:,1])))

#print("base line accuracy: ", max(sum(Y[:split,])/len(Y[:split,]),1 - sum(Y[:split,])/len(Y[:split,])))



