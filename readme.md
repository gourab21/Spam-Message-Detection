# Spam Detection Web App

This project is a web-based spam detection system that utilizes two models:
1. **LSTM Model** - A deep learning-based approach using TensorFlow and Keras.
2. **Traditional ML Model** - A machine learning-based approach using scikit-learn.

The application is built using Flask and allows users to enter a message and receive spam classification results from both models with confidence scores.

## Features
- Accepts user input through a simple web interface.
- Provides spam classification results from both an LSTM model and a traditional ML model.
- Displays confidence scores for each prediction.
- Includes a reset button to clear input and output.

## Installation
### Prerequisites
Ensure you have Python installed (preferably 3.8 or higher).

### Clone the Repository
```sh
git clone https://github.com/your-username/spam-detection-webapp.git
cd spam-detection-webapp
```

### Install Dependencies
Install the required Python packages using:
```sh
pip install -r requirements.txt
```

## Usage
### Run the Web App
```sh
python app.py
```
This will start a Flask development server. Open your browser and navigate to:
```
http://127.0.0.1:5000/
```

### Model Files
Ensure that the following model files are present in the project directory:
- `spam_classifier_lstm.keras` (LSTM model)
- `tokenizer.pkl` (Tokenizer for LSTM model)
- `spam_classifier.pkl` (Traditional ML model)

## Project Structure
```
├── app.py                  # Flask application
├── index.html              # Frontend template
├── requirements.txt        # Dependencies
├── spam_classifier_lstm.keras  # LSTM model file
├── spam_classifier.pkl     # Traditional ML model file
├── tokenizer.pkl           # Tokenizer for LSTM
└── README.md               # Documentation
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
Feel free to fork this repository and contribute by submitting pull requests. Improvements and bug fixes are welcome!

## Author
[Gourab Das] - [https://github.com/gourab21]

