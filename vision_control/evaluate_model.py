import pandas as pd,joblib
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.model_selection import train_test_split
D=pd.read_csv('data/gestures.csv',header=None); X=D.iloc[:,1:]; y=D.iloc[:,0]; a,b,c,d=train_test_split(X,y,test_size=.2,stratify=y,random_state=42); p=joblib.load('models/gesture_model.pkl').predict(b); print(classification_report(d,p)); print(confusion_matrix(d,p))
