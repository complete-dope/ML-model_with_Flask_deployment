import pickle
import numpy as np
from flask import Flask ,render_template , request ,jsonify

app = Flask(__name__)
model = pickle.load(open('model.pkl' , 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

# This is from where our model predicts the output
@app.route('/predict' , methods= ['POST'])
def predict():
    values = [float(x) for x in request.form.values()]
    values_final = [np.array(values)]
    prediction = model.predict(values_final)
    output = round(prediction[0])
    if ( output ==0 ):
        output ="Sorry to Inform you the person will NOT BE RETAINED "
    else:
        output="WOOH The person will be RETAINED"
    return render_template('index.html' , prediction_text = output)


@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/about')
def about():
    return render_template('about.html')



# their should a api call also here
# all the projects definitely make this api call route 
@app.route('/pred_api' , methods = ['POST'])
def api_pred():
    data = request.get_json()
    features = [np.array(list(data.values()))]
    prediction = model.predict(features)
    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)