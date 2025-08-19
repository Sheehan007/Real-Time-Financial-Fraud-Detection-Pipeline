import requests

def send_slack_alert(txn):
    webhook_url = "https://hooks.slack.com/services/your-id"  

    message = {
        "text": f"*FRAUD ALERT*\n*User:* {txn['user_id']}\n*Amount:* ${txn['amount']}\n*Location:* {txn['location']}"
    }

    response = requests.post(webhook_url, json=message)
    if response.status_code != 200:
        print(f"[Slack Error] {response.status_code}: {response.text}")

