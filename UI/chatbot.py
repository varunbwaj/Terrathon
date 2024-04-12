import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import classification_report
from string import punctuation
import re
def preprocess_train():
    nRowsRead = 3000 # specify 'None' if want to read whole file
    data = pd.read_csv('NLPConversation.csv', delimiter=',', nrows = nRowsRead)
    data.dataframeName = 'NLPConversation.csv'
    nRow, nCol = data.shape
    # print(f'There are {nRow} rows and {nCol} columns')
    data.rename(columns={"Context":"Questions","Response":"Answers"}, inplace=True)
    # data.head()
    # Preprocess the data
    data['Questions'] = data['Questions'].str.lower()
    data['Questions'] = data['Questions'].str.replace('[^\w\s]', '')
    data.dropna(inplace=True)
    intent_counts = data['Questions'].value_counts()
    data['Intent'] = data['Questions']
    questions_response_counts = data.groupby('Intent').size().reset_index(name='Count')
    avg_questions = data.groupby('Intent').size().mean()
    X_train, X_test, y_train, y_test = train_test_split(data['Questions'], data['Intent'], test_size=0.2, random_state=42)
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.svm import LinearSVC
    from sklearn.metrics import classification_report

    def vectorize_text(X_train, X_test):
        vectorizer = TfidfVectorizer()
        X_train_vec = vectorizer.fit_transform(X_train)
        X_test_vec = vectorizer.transform(X_test)
        return X_train_vec, X_test_vec, vectorizer

    def train_model(X_train_vec, y_train):
        model = LinearSVC()
        model.fit(X_train_vec, y_train)
        return model

    def evaluate_model(model, X_test_vec, y_test):
        y_pred = model.predict(X_test_vec)
        report = classification_report(y_test, y_pred)
        return report, y_pred

    # Vectorize the text data
    X_train_vec, X_test_vec, vectorizer = vectorize_text(X_train, X_test)

    # Train the model
    model = train_model(X_train_vec, y_train)

    return model,vectorizer,data

def predict(user_input,vectorizer,model,data):

    # Vectorize user input
    user_input_vec = vectorizer.transform([user_input.lower()])

    # Predict the intent
    predicted_intent = model.predict(user_input_vec)[0]

    # Implement response generation mechanism based on predicted intent
    if predicted_intent in data['Questions'].values:
        response = data[data['Questions'] == predicted_intent]['Answers'].values[0]
    else:
        response = "Sorry, I don't have information about this topic."
        
    return response


if __name__ == "__main__":
    model,vectorizer,data = preprocess_train()
    print(predict("What is your name?",vectorizer,model,data))
