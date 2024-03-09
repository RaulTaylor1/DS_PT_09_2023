from flask import Flask, request, render_template
import pickle
import os

os.chdir(os.path.dirname(__file__))
print(os.getcwd())

model = pickle.load(open('modelo.pkl', 'rb'))

print(model)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return '<h1>APP FLASK IRIS<h1>'

@app.route('/<name>', methods=['GET'])
def home():
    return '<h1>APP FLASK IRIS<h1>'

@app.route('/predict', methods=['POST'])
def predict():

    return model



if __name__ == '__main':
    app.run(debug=True)