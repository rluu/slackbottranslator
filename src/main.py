from pyslack import SlackClient
client = SlackClient('')
client.chat_post_message('#group3', "testing, testing...", username='group3slackbot')

