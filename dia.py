from flask import *
from pandas import *
from numpy import *
from sklearn import *
from pickle import *
import joblib
app=Flask(__name__)
model=joblib.load('diabetic.pkl')
@app.route('/')
def hello():
    return render_template('diabetic.html')
@app.route('/',methods=['POST','GET'])
def predict():
    print(request.form)
    fea = [float(x) for x in request.form.values()]
    fea[1] = (fea[1] - 117.81717) / 28.13464
    fea[2] = (fea[2] - 72.07154) / 11.32998
    fea[3] = (fea[3] - 20.324324) / 15.371490
    fea[5] = (fea[5] - 31.891414) / 6.403443
    fea[6] = (fea[6] - 0.42422165) / 0.24339996
    fea=[array(fea)]
    pred1=model.predict(fea)
    if pred1 == 0:
        return render_template('diabetic.html', pred='the person has no diabetics')
    else:
        return render_template('diabetic.html', pred='the person has diabetics')
if __name__ == '__main__':
    app.run(debug=True)