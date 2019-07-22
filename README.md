# Dogbot
A bot for slack related to dogs

# Background
As with most people working in tech, Slack has become omnipresent. Dogbot is a test app to look at the 
functionality of the Slack API. When you run the app it will post a random dog picture to the random channel in my own private slack space. 

# Usage
To use dogbot you should do the following. 
* Create your own workspace on [slack](https://slack.com/)
* Create an app and give it access to your space. 
* Save your bot token in an environment variable. Bot tokens start with `xoxb`
* Create a virtual environment and download the requirements in the requirements.txt file. 
* cd into the local directory and run `python dogbot.py`

# Reference
This documentation [page](https://api.slack.com/methods/chat.postMessage) should help to understand the API used in Dogbot. I have also used the [Dog CEO API](https://dog.ceo/dog-api/) to get dog images, as its easy to integrate and a really great resource.
