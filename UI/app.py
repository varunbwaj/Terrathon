from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import tensorflow as tf
import pandas as pd
from gtts import gTTS
from tensorflow.keras.preprocessing import image
import numpy as np
import os
from chatbot import preprocess_train, predict
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # replace with your own secret key

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'logged_in' in session:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('home'))

@app.route('/home', methods=['POST'])
def login():
    username = request.form.get('name')
    password = request.form.get('password')

    if username and password:
        session['logged_in'] = True
        return redirect(url_for('dashboard'))

    # If they are not valid, you could redirect them back to the login page
    return 'Login form submitted'


@app.route('/upload', methods=['POST'])
def upload():
    model = tf.keras.models.load_model("best.h5")
    model_down = tf.keras.models.load_model("best_down.h5")

    fs = request.files.get('snap')
    if fs:
        print('FileStorage:', fs)
        print('filename:', fs.filename)
        fs.save('image.jpg')

        img = image.load_img("image.jpg", target_size=(224,224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)

        prediction = model.predict(img)
        print(prediction)
        prediction_down = model_down.predict(img)
        print(prediction_down)
    
        combined_prediction = {"Result: Autism" : float(prediction[0][1]),
                       "Result: Down Syndrome" : float(prediction_down[0][1]),
                       "Neither Autism nor Down Syndrome" : float(1-prediction_down[0][1]-prediction[0][1])}
        threshold = 0.5
        predicted_classes = {class_name: probability for class_name, probability in combined_prediction.items() if probability > threshold}
    
        if not predicted_classes:
            predicted_classes = {'Neither Autism nor Down Syndrome': 1 - (prediction[0][1] + prediction_down[0][1])}
        
        return predicted_classes
    
    else:
        return 'You forgot Snap!'
    
@app.route('/send-message', methods=['POST'])
def send_message():
    message = request.json.get('message')
    print('Received message:', message)
    global predicted_message
    predicted_message =  predict(message,vectorizer,model1,data)
    return jsonify({'message':predicted_message}), 200


@app.route('/play-response', methods=['GET'])
def play_response():
    tts = gTTS(text=predicted_message,lang='en')
    tts.save('response.mp3')
    os.system("afplay response.mp3")
    return jsonify({'message': 'Response played'}), 200


if __name__ == '__main__':
    global model1
    global vectorizer
    global data
    model1,vectorizer,data = preprocess_train()
    app.run(debug=True)