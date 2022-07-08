from http import client
import logging
import json
from cgitb import text
from distutils.command.clean import clean
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import boto3
from botocore.exceptions import NoCredentialsError

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# Listens to incoming messages that contain "hello"
# To learn available listener arguments,
# visit https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
# @app.message("hello")
# def message_hello(message, say):
#     # say() sends a message to the channel where the event was triggered
#     say(f"Hey there <@{message['user']}>!")
#     say(f"Hey there 2")
# # Start your app
# if __name__ == "__main__":
#     SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()


@app.command("/com")
def handle_command(body, ack, client, logger):
    logger.info(body)
    ack()

    res = client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "gratitude-modal",
            "title": {"type": "plain_text", "text": "Landing Zone App"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "close": {"type": "plain_text", "text": "Cancel"},
            "blocks": [
                {
                    "type": "input",
                    "block_id": "my_block_0",
                    "element": {"type": "plain_text_input", "action_id": "comp_name", "placeholder": {"type":  "plain_text","text": "company name"}},
                    "label": {"type": "plain_text", "text": "Company Name"},
                },
                {
                    "type": "input",
                    "block_id": "my_block_1",
                    "element": {"type": "plain_text_input", "action_id": "email", "placeholder": {"type":  "plain_text","text": "your-email@domain.com"}},
                    "label": {"type": "plain_text", "text": "E-mail Address"},
                },
                {
                    "type": "input",
                    "block_id": "my_block_2",
                    "element": {"type": "plain_text_input", "action_id": "awsaccnum", "placeholder": {"type":  "plain_text","text": "7367799xxxxx"}},
                    "label": {"type": "plain_text", "text": "AWS-Account Number"},
                },
                {
                    "type": "input",
                    "block_id": "my_block_3",
                    "element": {"type": "plain_text_input", "action_id": "extid", "placeholder": {"type":  "plain_text","text": "cloudreach-(single word)"}},
                    "label": {"type": "plain_text", "text": "External ID"},
                },
                {
                    "type": "input",
                    "block_id": "my_block_4",
                    "element": {"type": "plain_text_input", "action_id": "cidr", "placeholder": {"type":  "plain_text","text": "10.0.0.0/16"}},
                    "label": {"type": "plain_text", "text": "CIDR Block"},
                },
                {
                    "type": "input",
                    "block_id": "my_block_5",
                    "element": {"type": "plain_text_input", "action_id": "whitelist", "placeholder": {"type":  "plain_text","text": "10.0.1.0/24-(Optional)"}},
                    "label": {"type": "plain_text", "text": "Whitelist"},
                },
                {
                    "type": "input",
                    "block_id": "my_block_6",
                    "element": {"type": "plain_text_input", "action_id": "vpcname", "placeholder": {"type":  "plain_text","text": "CR_VPC_Main"}},
                    "label": {"type": "plain_text", "text": "VPC Name"},
                },
                {
			"type": "input",
			"block_id": "my_block_8",
			"element": {
				"type": "static_select",
				"action_id": "static_select-action",
				"placeholder": {
					"type": "plain_text",
					"text": "Select a Region"
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "eu-west-1"
						},
						"value": "eu-west-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "eu-west-2"
						},
						"value": "eu-west-2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "us-west-1"
						},
						"value": "us-west-1"
					}
				]
			},
			"label": {
				"type": "plain_text",
				"text": "Region"
			}
		}
                ],
        },
    )
    logger.info(res)



# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
