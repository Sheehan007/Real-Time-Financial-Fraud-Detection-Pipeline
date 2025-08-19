# Real-Time-Financial-Fraud-Detection-Pipeline
A complete end-to-end streaming data pipeline for real-time detection of fraudulent financial transactions using Apache Kafka, Python, and Machine Learning, integrated with alerting and visualization systems.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


<h2>Tech Stack:</h2> 

1. Ingestion: Apache Kafka (Python kafka client)
2. Processing: Python (kafka consumer), scikit-learn
3. Detection: ML Model (RandomForestClassifier)
4. Alerting: Slack Webhook via alert_service.py
5. Dashboard: Streamlit Dashbaord
6. Storage: CSV file (farud_logs_2.csv) for logging




<h2>Project Objective:</h2>

- To simulate a banking system that detects fraudulent transactions in real-time using stream processing and machine learning, while:
- Streaming thousands of simulated transactions per minute
- Identifying anomalies or suspicious patterns
- Triggering alerts instantly (via Slack)
- Logging the events
- Visualizing activity on a real-time dashboard




<h2>How it works:</h2>
1. Transaction Producer (transaction_producer.py)

    Simulates random banking transactions and pushes them to a Kafka topic named transactions.

    Includes fields like:
    
        -transaction_id, user_id, amount, location, timestamp

    Runs continuously with a small delay (e.g., 0.5 seconds)

2. ML Fraud Detection Model (ml_model.py)

    Trains a RandomForestClassifier using labeled transaction data (legit or fraud) and saves the model as rf_fraud_model.pkl.


3. Kafka Consumer + Fraud Checker (consumer.py)

    Consumes incoming transactions, extracts features, and passes them to the trained model.

    If classified as fraud:
    
        -Sends a Slack alert via alert_service.py
    
        -Appends the transaction to fraud_logs.csv

    Else:
    
        -Logs as legit in the console


4. Slack Alerts (alert_service.py)

    Uses a Slack webhook to notify the team instantly when a fraudulent transaction is detected.


5. Streamlit Dashboard (dashboard.py)

    Displays transactions detected as fraud in real-time using the fraud_logs.csv.
    
    Visualizations include:
    
        -Count of frauds over time
        
        -Location-wise fraud heatmap
        
        -User-wise fraud history



































