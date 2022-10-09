from flask import Flask,render_template,request,url_for
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('finalized_model.pkl', 'rb'))


app=Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method=='POST':
        Age=int(request.form['Age'])
        sex=request.form['sex']
        if sex=='Male'or sex=='male':
            sex=0
        else:
            sex=1
        BMI=float(request.form['bmi'])
        children=int(request.form['children'])
        smoker=request.form['smoker']
        if smoker=='yes':
            smoker=0
        else:
            smoker=1
        region=request.form['region']
        if region=='southeast':
            region=0
        elif region=='southwest':
            region=1
        elif region=='northeast':
            region=2
        elif region=='northwest':
            region=3
        prediction=model.predict([[Age,sex,BMI,children,smoker,region]])
        output=prediction[0]
        return render_template('index.html',prediction_text="Your medical Expenses Charges are {}".format(output))
    else:
        return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True) 