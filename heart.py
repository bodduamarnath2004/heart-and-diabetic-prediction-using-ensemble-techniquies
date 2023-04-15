from flask import *
from pandas import *
from numpy import *
from sklearn import *
from pickle import *
import joblib
app=Flask(__name__)
model=joblib.load('model3.pkl')
@app.route('/')
def hello():
    return render_template('heart.html')
@app.route('/',methods=['POST','GET'])
def predict():
    print(request.form)
    fea = [float(x) for x in request.form.values()]
    fea=[array(fea)]
    pred1=model.predict(fea)
    if pred1 == 0:
        return render_template('heart.html', pred='the person has no heart stroke')
    else:
        return render_template('heart.html', pred='the person has heart stroke')
if __name__ == '__main__':
    app.run(debug=True)