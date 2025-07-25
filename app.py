import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def main():
    return render_template("./index.html")

@app.route('/home',methods=['POST'])
def home():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('./index1.html',prediction_text='House price should be $ {}'.format(output))


if __name__ == "__main__":
    app.run(debug=True)