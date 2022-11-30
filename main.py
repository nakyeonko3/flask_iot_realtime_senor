from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

name = "nakyeonko"

@app.route('/')
def mainPage():
    return render_template('index.html', name = name)

@app.route('/getSensorData')
def getSensorData():
    return jsonify({'sensor_data':random.randint(0, 9)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)