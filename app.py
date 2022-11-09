

from flask import Flask,render_template,url_for,jsonify,request
import pickle
import pandas as pd
import numpy as np
app=Flask(__name__)
model=pickle.load(open('xg_boost.pkl','rb'))
@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/calorie')
def calorie_reco():
    return render_template('calorie.html')

@app.route('/predict',methods=['POST'])

def predict():
    if request.method=='POST':
        Gender=request.form['Gender']
        if Gender=="Male":
            Gender=1
        else:
            Gender=0
        age=float(request.form['Age'])
        height=float(request.form['Height'])
        Weight=float(request.form['Weight'])
        work_duration=int(request.form['Duration'])
        Heart_rate=float(request.form['Heart'])
        Body_temp=int(request.form["Body"])
        

        prediction_va=model.predict(np.array([Gender,age,height,Weight,work_duration,Heart_rate,Body_temp]).reshape(1,-1))
        return render_template('calorie.html',prediction_text='Your have burned {} Calories'.format(prediction_va[0]))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)