from flask import Flask, render_template, request
from tensorflow import keras
import csv
import io
import numpy as np

model = keras.models.load_model('model.h5')

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template("index.html")

@app.post('/result')
def result():
    age = int(request.form.get('Age'))
    sex = int(request.form.get('Sex'))
    bp = int(request.form.get('BP'))
    cholesterol = int(request.form.get('Cholesterol'))
    natok = int(request.form.get('NaToK'))
    
    # test_input = request.files.get('test_input_file')
    # test_input.stream.seek(0)
    # test_stream = io.StringIO(test_input.stream.read().decode('UTF8'))
    # csv_reader = csv.DictReader(test_stream, delimiter=',', quotechar='"')
    # for row in csv_reader:
    #     b_pressure = row['blood pressure']
    #     fever = row['fever']
    #     diabetes = row['diabetes']
    #     vomit = row['vomit']

    inputs = np.expand_dims(np.array([age, sex, bp, cholesterol, natok]), axis=0)
    prediction = model.predict(inputs)

    return f'{prediction}'