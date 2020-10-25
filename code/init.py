
#header files required
import pandas as pd
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
import re
import string
import word2vec
import random
from nltk.tokenize import WordPunctTokenizer
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer 
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

vec_size = 100
w2v_model = word2vec.load('cleaned.bin')
LR_model = None

def lemmatize_sentence(tweet_tokens, stop_words = ()):
    lemmatizer = WordNetLemmatizer()
    cleaned_tokens = []
    for token, tag in pos_tag(tweet_tokens):
        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('V'):
            pos = 'v'
        else:
            pos = 'a'
        token = lemmatizer.lemmatize(token, pos)
        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


def init_depression():

    df = pd.read_csv('cleaned_data.csv')
    # Converting the the columns to usable lists in sklearn
    text = df.TEXT.tolist()
    sentiment = df.SENTIMENT.tolist()

    # Run these if you want to train the update the model based on new CLEANED data

    # my_filtered_csv = pd.read_csv('./betterdata.csv', usecols=['SENTIMENT', 'TEXT'])
    # word2vec.word2phrase('cleaned_data.csv', 'cleaned-phrases', verbose=True)
    # word2vec.word2vec('cleaned-phrases', 'cleaned.bin', size=vec_size, binary=True, verbose=True)
    # word2vec.word2clusters('cleaned_data.csv', 'cleaned-clusters.txt', 100, verbose=True)




    cleaned_values = []
    cleaned_labels = [] 
    for ind_1, sentences in enumerate(text):
        cur_sentence = [0] * vec_size
        num_words = 0
        for word in sentences.split(' '):
            word.strip(' ')
            if len(word) == 0:
                continue
            if word not in w2v_model.vocab:
                continue
            cur_sentence = [a + b for a, b in zip(cur_sentence, w2v_model[word])]
            num_words += 1
        if num_words == 0:
            continue
        for ind, val in enumerate(cur_sentence):
            cur_sentence[ind] = val / num_words
        cur_sentence.append(sentiment[ind_1])
        cleaned_values.append(cur_sentence)
        cleaned_labels.append(sentiment[ind_1])


    df = pd.DataFrame(cleaned_values)
    scaled_features = StandardScaler().fit_transform(df.values)
    scaled_features_df = pd.DataFrame(scaled_features, index=df.index, columns=df.columns)

    train_features =df.sample(frac=0.8,random_state=42)
    test_features = df.drop(train_features.index)

    X_train = train_features[range(0, vec_size)]
    Y_train = train_features[vec_size]
    X_val = test_features[range(0, vec_size)]
    Y_val = test_features[vec_size]

    global LR_model
    LR_model = LogisticRegression(max_iter=10000)
    LR_model.fit(X_train, Y_train)

def sentence_clean(sentence):
    tokenizer = WordPunctTokenizer() 
    cleaned = []
    sentence = re.sub('^https?://.*[rn]*','', sentence)
    sentence = re.sub("(@[A-Za-z0-9_]+)","", sentence)
    sentence = re.sub("([^\w\s])", "", sentence)
    sentence = tokenizer.tokenize(sentence)
    
    cleaned = []
    # stop_words = stopwords.words('english')
    sent = lemmatize_sentence(sentence)
    result = ''
    if len(sent) > 0:
        result = ' '.join(sent)
    return result



def depression_scale(sentence):
    # cleaning the sentence
    clean_sentence = sentence_clean(sentence)
    word_vector = [0] * vec_size
    num_words = 0
    for word in clean_sentence.split(' '):
        word.strip(' ')
        if len(word) == 0:
            continue
        if word in w2v_model.vocab:
            word_vector = [a + b for a, b in zip(word_vector, w2v_model[word])]
        else:
            continue
        num_words += 1
    if num_words == 0:
        return 2

    global LR_model    
    for ind, val in enumerate(word_vector):
        word_vector[ind] = val / num_words
    y_result_probs = 4 * LR_model.predict_proba([word_vector])[0][1]
    print(y_result_probs)
    return y_result_probs

