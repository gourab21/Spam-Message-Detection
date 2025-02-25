from flask import Flask, render_template, request, redirect, url_for
import tensorflow as tf
import joblib
import pickle
import os
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define model paths dynamically
LSTM_MODEL_PATH = os.path.join(BASE_DIR, "spam_classifier_lstm.keras")
TOKENIZER_PATH = os.path.join(BASE_DIR, "tokenizer.pkl")
ML_MODEL_PATH = os.path.join(BASE_DIR, "spam_classifier.pkl")

# Load LSTM model and tokenizer
lstm_model = tf.keras.models.load_model(LSTM_MODEL_PATH)
with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)

# Load traditional ML model
ml_model = joblib.load(ML_MODEL_PATH)

def predict_lstm(message, max_len=100):
    sequence = tokenizer.texts_to_sequences([message])
    padded_sequence = pad_sequences(sequence, maxlen=max_len)
    prediction = lstm_model.predict(padded_sequence)[0][0]
    return "Spam" if prediction > 0.5 else "Not Spam", prediction

def predict_ml(message):
    prediction = ml_model.predict([message])
    probability = ml_model.predict_proba([message])
    spam_prob = probability[0][1] * 100
    ham_prob = probability[0][0] * 100
    return "Spam" if prediction[0] == 1 else "Not Spam", spam_prob if prediction[0] == 1 else ham_prob

@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    lstm_result = None
    lstm_confidence = None
    ml_result = None
    ml_confidence = None
    if request.method == "POST":
        if "reset" in request.form:
            return redirect(url_for("index"))
        message = request.form["message"]
        lstm_result, lstm_confidence = predict_lstm(message)
        ml_result, ml_confidence = predict_ml(message)
    return render_template("index.html", message=message, lstm_result=lstm_result, lstm_confidence=lstm_confidence,
                           ml_result=ml_result, ml_confidence=ml_confidence)

if __name__ == "__main__":
    app.run(debug=True)