import pandas as pd,joblib
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report
D=pd.read_csv('data/gestures.csv',header=None); X=D.iloc[:,1:]; y=D.iloc[:,0]; a,b,c,d=train_test_split(X,y,test_size=.2,stratify=y,random_state=42)
model=make_pipeline(StandardScaler(),SVC(kernel='rbf',probability=True)); model.fit(a,c); print(classification_report(d,model.predict(b))); joblib.dump(model,'models/gesture_model.pkl')
