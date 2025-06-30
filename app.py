import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        city = int(request.form.get('city'))
        category = int(request.form.get('category'))
        branch = int(request.form.get('branch'))
        rank = int(request.form.get('rank'))

        final_features = np.array([[city, category, branch, rank]])
        prediction = model.predict(final_features)

        return render_template('result.html', prediction_text=f'Predicted College: {prediction[0]}')

    except Exception as e:
        return render_template('result.html', prediction_text=f'Error: {str(e)}')

if __name__ == "__main__":
    app.run(debug=True)
