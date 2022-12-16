from flask import Flask, render_template, request
import csv
import io

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index(name=None):
    return render_template("index.html")

@app.post('/result')
def result():
    data = request.form
    b_pressure = request.form.get('Bpressure')
    fever = request.form.get('Fever')
    diabetes = request.form.get('Diabetes')
    vomit = request.form.get('Vomit')
    classifier = request.form.get('classifier')
    
    test_input = request.files.get('test_input_file')
    test_input.stream.seek(0)
    test_stream = io.StringIO(test_input.stream.read().decode('UTF8'))
    csv_reader = csv.DictReader(test_stream, delimiter=',', quotechar='"')
    for row in csv_reader:
        b_pressure = row['blood pressure']
        fever = row['fever']
        diabetes = row['diabetes']
        vomit = row['vomit']

    return f'{b_pressure} {fever} {diabetes} {vomit} {classifier}'