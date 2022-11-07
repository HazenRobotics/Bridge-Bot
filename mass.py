from slack_sdk import WebClient
from slack_sdk.audit_logs.v1.logs import App

oken_app = 'xapp-1-A041WRBKX8E-4088132000401-45c7ddf98e15a7a888d0c4897d5b22092db96bbb2ff933015b1a0b17e34585e5'
token_slack = 'xoxb-1032863990657-4071370518627-ZmZ2ZB6Di4vfqrev5Z2k1wPq'
token_discord = 'MTAxOTI0MzU0NzA0OTg3MzUyOQ.Gh4R60.CA9rY-u5kO2ySgNI7i6iOZolrHrFsDdeH1-480'

slack = WebClient(token=token_slack)
app = App(token=token_slack, signing_secret="")
response = slack.conversations_list()
conversations = response["channels"]

for i in conversations:
    file = open(str(i['id']), "w+")
    print(len(slack.conversations_history(channel=i['id'])['messages']))

