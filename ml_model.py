import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# simulating a dataset
np.random.seed(42)
n = 10000
data = pd.DataFrame({
    'user_id': np.random.randint(1000, 9999, size=n), 
    'amount': np.random.exponential(100, size=n), 
    'location': np.random.choice(['NY', 'LDN', 'SG', 'DEL', 'DXB'], size=n), 
    'label': np.random.choice([0,1], size=n, p=[0.98, 0.02])
})

data['loc_code'] = data['location'].astype('category').cat.codes
X = data[['amount', 'loc_code']]
y = data['label']

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2)

# model training
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

def send_alert(txn):
    print(f"ALERT! Fraud detected:\nUser {txn['user_id']} | Amount: {txn['amount']} | Location: {txn['location']}")

joblib.dump(clf, 'rf_fraud_model.pkl')




