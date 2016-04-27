import time
from slackclient import SlackClient
token='xoxp-19745829781-38048263175-38056115377-d6ad0242f9'
sc = SlackClient(token)
print sc.api_call("api.test")
sc.api_call?
print sc.api_call("chat.postMessage", channel="#group3", text="Hello from slack client", username="ismav29", icon_emoji=':robot_face:')

