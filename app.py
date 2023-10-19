import numpy as np
import pandas as pd
import streamlit as st
import pickle
import sklearn
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Download NLTK data files
nltk.download('punkt')

# importing required pickle files:

model = pickle.load(open('mnb.pkl','rb'))
tfidf = pickle.load(open('tfidf.pkl','rb'))

# Adding title image:

x, y, z = st.columns(3)

with x:
    st.write(' ')

with y:
    st.markdown('<p style="text-align: center; font-size: 22px; font-weight: bold;">SPAM SMS CLASSIFIER</p>', unsafe_allow_html=True)

with z:
    st.write(' ')



# taking SMS as input from user

sms = st.text_area("Please enter the SMS here:", height=150)

# defining list of stopwords:

stopwords = [
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
    "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this",
    "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the",
    "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for",
    "with", "about", "against", "between", "into", "through", "during", "before", "after",
    "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any",
    "both", "each", "few", "more", "most", "other", "some", "such", "nor", "only", "own",
    "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"
]

# defining the function for textual preprocessing of the user input sms:

def text_processing(sent):
    # conversion into lower case
    sent = sent.lower()

    # punctuations removal
    sent = re.sub("[^a-zA-Z0-9]", " ", sent)

    # tokanization
    sent = nltk.word_tokenize(sent)

    # assigning empty list:
    empty = []

    # stop words removal:
    for i in sent:
        if i not in stopwords:
            empty.append(i)

    # stemming:
    ps = PorterStemmer()

    empty = [ps.stem(word) for word in empty]

    return " ".join(empty)

# applying function on user input:
user_sent = text_processing(sms)

# applying vectorization:
vector = tfidf.transform([user_sent]).toarray()

# model prediction

result = int(model.predict(vector)[0])

# creating a button

button_style = """
        <style>
        div.stButton > button:first-child {
            background-color: green !important;
            color: black !important;
        }
        </style>
    """

# Display the button with the custom style
st.markdown(button_style, unsafe_allow_html=True)

# creating a condition application when the button is pressed:

if st.button("Classify"):

    if result==0:
        col1, col2, col3 = st.columns(3)

        with col1:
            st.write(' ')

        with col2:
            st.markdown("<p style='text-align: center; font-size: 18px; font-weight: bold;'>Not Spam</p>",
                        unsafe_allow_html=True)
            st.image("not spam.png", width=200)

        with col3:
            st.write(' ')
    else:
        col3, col4, col5 = st.columns(3)

        with col3:
            st.write(' ')

        with col4:
            st.markdown("<p style='text-align: center; font-size: 18px; font-weight: bold;'>Spam</p>",
                        unsafe_allow_html=True)
            st.image("spam image.png", width=200)

        with col5:
            st.write(' ')
