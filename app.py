import numpy as np
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
import pandas as pd
from flask import Flask,request,jsonify,render_template
from flask_bootstrap import Bootstrap
import pickle

app=Flask(__name__)
Bootstrap(app)
def text_process(mess):
    """
    1. remove punc
    2.remove stop words
    3. return list of clean text words
    """
    nopunc=[char for char in mess if char not in string.punctuation]
    nopunc=''.join(nopunc)
    text=[word for word in nopunc.split() if word.lower() not in stopwords.words('English')]
    return text
model=pickle.load(open('modelfinal.pkl','rb'))



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    test=request.form.values()
    test_ser=pd.Series(test)
   
    pred=model.predict(test_ser)
    output=pred[0]
    if output==1:
        result='True'
    else:
        result='Fake'
    return render_template('index.html',prediction_text='Above News is {}!'.format(result))


if __name__=='__main__':
    app.run(debug=True)
    
