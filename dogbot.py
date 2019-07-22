import os
import requests
import slack


slack_token = os.environ["SLACK_BOT_TOKEN"]
client = slack.WebClient(token=slack_token)

def doggo():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    return data['message']

dp = doggo()

client.chat_postMessage(
  channel="CCCN3EXK2", # Random channel
  text= dp,
  attachments=[{"text": "Dogbot - dog picture in yor moment of need!"}]
)
