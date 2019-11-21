
import os

from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Embedding, SpatialDropout1D, Flatten
from keras.layers import Input
from keras.callbacks import EarlyStopping, ModelCheckpoint
from keras.layers.convolutional import Conv1D
from keras.layers.convolutional import MaxPooling1D
from keras.layers.merge import concatenate
#from keras.utils.vis_utils import plot_model
from keras.models import Model, load_model

from app.dictionaries import load_dictionaries
from app.storage_service import weights_filepath

ORIGINAL_WEIGHTS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "model", "weights", "weights-improvement-01-0.91.hdf5")
FINAL_MODEL_FILEPATH = os.path.join(os.path.dirname(__file__),"..", "model", "final_model.h5")
FINAL_WEIGHTS_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "model", "weights", "weights-reconstructed.hdf5")

def production_model():
	model = unweighted_model()
	print("LOADING MODEL WEIGHTS...")
	model.load_weights(weights_filepath())
	return model

def reconstructed_final_model(idempotent=True):
    if idempotent == False:
        recreate_weights(FINAL_WEIGHTS_FILEPATH)
    model = unweighted_model()
    model.load_weights(FINAL_WEIGHTS_FILEPATH)
    return model

def recreate_weights(weights_filepath):
	print("SAVING FINAL MODEL WEIGHTS TO:", weights_filepath)
	model = saved_final_model()
	model.save_weights(weights_filepath)
	return True

def saved_final_model():
	print("LOADING FINAL MODEL...")
	return load_model(FINAL_MODEL_FILEPATH)

def original_model():
	model = unweighted_model()
	print("LOADING MODEL WEIGHTS...")
	model.load_weights(ORIGINAL_WEIGHTS_FILEPATH, by_name=True)
	return model

def unweighted_model():
	dictionary, dictionary_s = load_dictionaries()
	dictionary_size, dictionary_size_s = len(dictionary), len(dictionary_s)

	print("CONSTRUCTING THE MODEL...")
	#import model architecture
	seq_len = 20
	#input1
	inputs1 = Input(shape=(seq_len,))
	#embedding1 = Embedding(dictionary_size + 1, 128)(inputs1)
	embedding1 = Embedding(dictionary_size + 1, 64)(inputs1) # changed from 128 to 64 to match saved weights file
	conv1 = Conv1D(filters=32, kernel_size=3, activation='relu', padding='valid')(embedding1)
	drop1 = Dropout(0.2)(conv1)
	pool1 = MaxPooling1D(pool_size=2)(drop1)
	flat1 = Flatten()(pool1)
	#Input2
	inputs2 = Input(shape=(seq_len,))
	#embedding2 = Embedding(dictionary_size_s + 1, 128)(inputs2)
	embedding2 = Embedding(dictionary_size_s + 1, 64)(inputs2) # changed from 128 to 64 to match saved weights file
	conv2 = Conv1D(filters=32, kernel_size=3, activation='relu', padding='valid')(embedding2)
	drop2 = Dropout(0.2)(conv2)
	pool2 = MaxPooling1D(pool_size=2)(drop2)
	flat2 = Flatten()(pool2)
	#merge via concatenation
	merged = concatenate([flat1, flat2])
	#dense
	dense1 = Dense(64, activation='relu')(merged)
	dense2 = Dense(32, activation='relu')(dense1)
	outputs = Dense(2, activation='softmax')(dense2)
	model = Model(inputs=[inputs1, inputs2], outputs=outputs)
	#print(model.summary())

	return model
