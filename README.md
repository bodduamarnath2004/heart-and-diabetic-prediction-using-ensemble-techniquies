# heart-and-diabetic-prediction-using-ensemble-techniquies
The objective of the project is to create a website that is linked with machine learning model and predicts whether a person has heart stroke or diabetics based on the details entered by them in the web portal.
The main motive is to reduce the number of deaths due to these diseases , and that can be achieved by knowing the disease in the primary state and taking proper diagnosis for the disease in proper interval of time.

The method used here was machine learning modeling where initially a dataset was selected for training the model and then the dataset was cleaned using datapreprocessing methods and then the unneccesary data was removed, and transformed.
Later the well formed dataset was splitted into training and testing data and then fit into ExtraTreeClassifier and was used for Diabetics prediction and another model known as random forest classifier was used for Heart stroke prediction.
Then this model was linked to html code using pickel package and then the code was deployed using amazon web services and the website was finally created.

%The results of the model can be described based on the accuracy achieved y the models
For diabetics Prediction, ExtraTrees Classifier has given an accuracy of 85.79%
For diabetics Prediction, RandomForest Classifier has given an accuracy of 98.46%
