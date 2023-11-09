from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/pred", methods=['POST'])
def predict():
    Administrative = request.form['Administrative']
    Administrative_Duration = request.form['Administrative_Duration']
    Informational = request.form['Informational']
    Informational_Duration = request.form['Informational_Duration']
    ProductRelated= request.form['ProductRelated']
    ProductRelated_Duration = request.form['ProductRelated_Duration']
    BounceRates = request.form['BounceRates']
    ExitRates =  request.form['ExitRates']
    PageValues =  request.form['PageValues'] 
    SpecialDay = request.form['SpecialDay']
    Month = request.form['Month']
    OperatingSystems = request.form['OperatingSystems']
    Browser = request.form['Browser']
    Region = request.form['Region']
    TrafficType= request.form['TrafficType']
    VisitorType = request.form['VisitorType']
    Weekend = request.form['Weekend']
    
    # Convert categorical variables to integers
    Month = int(Month)
    OperatingSystems = int(OperatingSystems)
    Browser = int(Browser)
    Region = int(Region)
    TrafficType = int(TrafficType)
    VisitorType = int(VisitorType)
    Weekend = int(Weekend)
    
    total = [[int(Administrative), float(Administrative_Duration), int(Informational), float(Informational_Duration),
            int(ProductRelated), float(ProductRelated_Duration), float(BounceRates), float(ExitRates), float(PageValues),
            float(SpecialDay), Month, OperatingSystems, Browser, Region, TrafficType, VisitorType, Weekend]]
    
    print(total)
    prediction = model.predict(total)
    print(prediction)
    
    if prediction == 0:
        text = 'The visitor is not interested in buying products.'
    else:
        text = 'The visitor is interested in buying products.'
    
    return render_template('submit.html', prediction_text=text)

if __name__ == "__main__":
    app.run(debug=True)
