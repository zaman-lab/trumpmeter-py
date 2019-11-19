
from wordsegment import load, segment
import pandas as pd
import numpy as np
import re
#import progressbar
from gensim import corpora
import string
from keras.preprocessing import sequence
import sys
import os


import nltk
#nltk.download()
from nltk.corpus import stopwords

# In[240]:
def get_xy(n, save = False):
    '''
    n = size of the data you want to process 
    save = Whether you want the generated X and Y to be saved in you directory for future use. 
    '''
    # data = pd.read_csv('Data/modeling_1_copie.csv', nrows=n, index_col = 0)
    print(os.listdir())
    temp=pd.read_csv('Data/labeled_data_balanced.csv', index_col = 0, encoding='latin')
    if(len(temp.dropna(axis=0, how='any'))<len(temp)):
        print(len(temp.dropna(axis=0, how='any')),len(temp))
        print('NAN PROBLEM - RECHECK CSV')

    data_1 = temp.loc[temp['rep/dem']==1].sample(int(0.5*n))
    data_0 = temp.loc[temp['rep/dem']==0].sample(int(0.5*n))
    data=pd.concat([data_0,data_1]).sample(frac=1)
        


    print('size of data is: ', data.shape)


    # ## wordsegment
    load()

    def my_replace(match):
        match = match.group()
        return ' '.join(segment(match))

    def process_rep(twt):
        try:
            return(re.sub('#\w+', my_replace, twt))
        except Exception as e:
            #print(e)
            return(None)

    print('segmenting ...')
    data['tweet_s'] = data.tweet.apply(process_rep)



    # ## Cleaning

    def clean(twt):
        #print('Before :', twt)
        #remove punctutation
        try:
            twt = twt.translate(str.maketrans('','',string.punctuation))
            twt = twt.split()
            twt = [i.lower() for i in twt]
            twt = [i for i in twt if 'htt' not in i and 
                                          i not in stopwords.words('english')]
            twt = ' '.join(twt)
            return(twt)
        except Exception as e:
            #print(e)
            print(e)
            print(twt)
            return(None)


    # ### For X




    print('cleaning ..')
    #bar = progressbar.ProgressBar()
    l = []
    
    for i in range(data.shape[0]):
        twt = data.iloc[i]
        a = clean(twt['tweet'])
        #print(twt)
        if a != None:
            l.append([a.split(), twt['rep/dem']])
        #else:
          #print('warning')
        if i% 50000==0:  
          print("{} cleaned out of {}".format(i,data.shape[0]))

    print('length of l is ',len(l))

    # In[247]:

    print('making dictionaries for non-segment')
    d_id = pd.DataFrame(l, columns = ['twt', 'rep/dem'])
    dictionary = corpora.Dictionary(d_id.twt)
    dictionary.save('Dictionary/dic.txt')
    # dictionary = corpora.Dictionary.load('Dictionary/dic.txt')
    print('dic made')                
    dictionary_size = len(dictionary.keys())
    print("dictionary size: ", dictionary_size)


    # ### For X_s

    # In[248]:


    print('cleaning ..')
    #bar = progressbar.ProgressBar()
    l = []
    for i in range(data.shape[0]):
        twt = data.iloc[i]
        a = clean(twt['tweet_s'])
        # if(a != clean(twt['tweet'])):
            # print(bkbaka)
        if a != None:
            l.append([a.split(), twt['rep/dem']])
        if i% 50000==0:  
          print("{} cleaned out of {}".format(i,data.shape[0]))


    # In[249]:

    print('making dictionaries for segment')
    d_id_s = pd.DataFrame(l, columns = ['twt', 'rep/dem'])
    dictionary_s = corpora.Dictionary(d_id_s.twt)
    dictionary_s.save('Dictionary/dic_s.txt')
    print('dic made')                
    dictionary_size_s = len(dictionary_s.keys())
    print("dictionary size: ", dictionary_size_s)

    #get seq_len 

    mean_length = d_id.twt.apply(lambda x: len(x)).mean()
    sd_length = d_id.twt.apply(lambda x: len(x)).std()
    seq_len = np.round((mean_length + 2*sd_length)).astype(int)

    mean_length = d_id_s.twt.apply(lambda x: len(x)).mean()
    sd_length = d_id_s.twt.apply(lambda x: len(x)).std()
    seq_len_s = np.round((mean_length + 2*sd_length)).astype(int)

    #we choose the bigger sequence length
    seq_len = max(seq_len, seq_len_s)

    print('the sequence length we will use is ', seq_len)


    def transform(twt, seq_len):
        #twt = clean(twt).split()
        l = []
        for i in twt:
            try:
                l.append(1 + dictionary.token2id[i])
            except:
                l.append(0)
        twt = sequence.pad_sequences([l], maxlen=seq_len)
        return(twt)


    print('transforming non-segmented to numerical')
    d_id.twt = d_id.twt.apply(lambda x: transform(x, seq_len))



    # In[254]:


    def transform_s(twt, seq_len):
        #twt = clean(twt).split()
        l = []
        for i in twt:
            try:
                l.append(1 + dictionary_s.token2id[i])
            except Exception as e:
                print(e)
                l.append(0)
        twt = sequence.pad_sequences([l], maxlen=seq_len)
        return(twt)


    # In[255]:

    print('transforming segmented to numerical')
    d_id_s.twt = d_id_s.twt.apply(lambda x: transform_s(x, seq_len))


    print('making X and Y ... ')
    X = np.vstack(d_id.twt.apply(lambda x : x[0]).values)
    Y = np.array(d_id['rep/dem'])
    print('X matrix: ', X.shape)
    print('Y vector: ', Y.shape)

    X_s = np.vstack(d_id_s.twt.apply(lambda x : x[0]).values)
    Y_s = np.array(d_id_s['rep/dem'])
    print('Xs matrix: ', X_s.shape)
    print('Ys vector: ', Y_s.shape)

    if save: 
        print('saving X and Y')
        np.save('X', X)
        np.save('Y', Y)

        print('saving X_s and Y_s')
        np.save('X_s', X_s)
        np.save('Y_s', Y_s)

    return(X, X_s, Y, dictionary_size, dictionary_size_s, seq_len)


#get_xy(n = 100, save = False)
