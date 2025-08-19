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
