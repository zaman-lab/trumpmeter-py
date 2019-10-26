#!/usr/bin/env python
# coding: utf-8

# #upload libraries
import sqlite3
import pandas as pd
import numpy as np
import json
from os import listdir
from os.path import isfile, join
from itertools import islice
import re
import h5py
from gensim.corpora import Dictionary
from keras.utils import np_utils
from helper_text import main_clean
#from model import load_model
from keras.models import load_model

model = load_model("Final_weights/final_model.h5")
model_len=20

#-----------------Example Testing-------------------------
print('Example: ')
twt = 'He is awesome, make american great again. Democrats is taking off. We love democrats.'
print(twt)

x, x_s = main_clean(twt,model_len)
#predict

print(model.summary())

pro_pol = model.predict([x, x_s])[:,0]
print('the probability this tweet is pro Trump is ', pro_pol)




####---------------------Method 3: Read from csv file and generate prediction into the csv file
#### The CSV file should contain many columns, but at least these columns, (1) "tweets"
#### The Output will be generated back into the inputfilename+'_output.csv', with  new column (1)"pred_label" (2)"pred_prob_0"

input_file="TrumpTweets.csv"
twt_df=pd.read_csv(input_file)
twt_df['pred_label']=0
twt_df['pred_prob_0']=0
for idx, row in twt_df.iterrows():
    twt=twt_df.loc[idx,'tweet']
    x, x_s = main_clean(twt,model_len)
    pred_prob_0 = model.predict([x, x_s])[:,0]
    pred_label = int(pred_prob_0<0.5)
    twt_df.loc[idx,'pred_label']=pred_label
    twt_df.loc[idx,'pred_prob_0']=pred_prob_0

output_file=input_file.split('.')[-2]+'_output.csv'
twt_df.to_csv(output_file)





