import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

import config

# Find mechanism to pass this as token.
slack_token = config.slack_token #os.environ["SLACK_BOT_TOKEN"]
client = WebClient(token=slack_token)

general_id = config.general_channel
message = 'test 123'

class SendMessage():
    def send(self, message, channel_id):
        try:
            response = client.chat_postMessage(
                channel= channel_id,
                text= message
            )
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response["error"]    # str like 'invalid_auth', 'channel_not_found'

'''
def test():
    obj = SendMessage()
    obj.send(message, channel_id=general_id)

test()
'''