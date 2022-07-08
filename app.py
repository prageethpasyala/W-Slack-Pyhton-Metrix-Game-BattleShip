from http import client
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import json
import boto3

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
import numpy as np

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

dynamodb = boto3.resource('dynamodb',region_name='eu-west-2')
table = dynamodb.Table("Coordinates")

# ----------------------------------------- pirate ----------------------------------------------------------------------------------
@app.message("pirate")
def message_hello(message, say):

    say(
		blocks = [
			{
				"type": "divider"
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*<fakeLink.toUserProfiles.com| Welcome to the game, Let's battle :>*"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": ":skull: *Pirate* \n Let's deploy pirate ships"
				},
				"accessory": {
					"type": "button",
					"action_id": "pirate",
					"text": {
						"type": "plain_text",
						# "emoji": true,
						"text": "Play"					
					},
					"value": "click_me_123"
				}
			},
			
			
		]
	)

    # ---------------
@app.action("pirate")
def handle_command(body, ack, client, logger):
    logger.info(body)
    ack()

    res = client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "gratitude-modal-pirate",
            "title": {"type": "plain_text", "text": "BattleShip Matrix"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "close": {"type": "plain_text", "text": "Cancel"},
            "blocks": [
                {
                    "type": "input",
                    "block_id": "my_block_0",
                    "element": {"type": "plain_text_input", "action_id": "c1", "placeholder": {"type":  "plain_text","text": "Coordinate digts must be between 0-4 eg. 3 2"}},
                    "label": {"type": "plain_text", "text": ":pushpin: 1st Coordinate"},
                },
                {
                    "type": "input",
                    "block_id": "my_block_1",
                    "element": {"type": "plain_text_input", "action_id": "c2", "placeholder": {"type":  "plain_text","text": "Coordinate digts must be between 0-4 eg. 3 2"}},
                    "label": {"type": "plain_text", "text": ":pushpin: 2nd Coordinate"},
                },
                {
                    "type": "input",
                    "block_id": "my_block_2",
                    "element": {"type": "plain_text_input", "action_id": "c3", "placeholder": {"type":  "plain_text","text": "Coordinate digts must be between 0-4 eg. 3 2"}},
                    "label": {"type": "plain_text", "text": ":pushpin: 3rd Coordinate"},
                }
                ]
        }
    )
    logger.info(res)



@app.view("gratitude-modal-pirate")
def view_submission(ack, body, client, logger, say):
    ack()
        
    logger.info(body["view"]["state"]["values"])
    # Extra Credit: Uncomment out this section
    cloudreach_client_records = "C036HNB7LB1"
    user_text_0 = body["view"]["state"]["values"]["my_block_0"]["c1"]["value"]
    user_text_1 = body["view"]["state"]["values"]["my_block_1"]["c2"]["value"]
    user_text_2 = body["view"]["state"]["values"]["my_block_2"]["c3"]["value"]
    
    client.chat_postMessage(channel=cloudreach_client_records, text=":pushpin: Your Coordinates :")
    client.chat_postMessage(channel=cloudreach_client_records, text="- 1st Coordinate : "+user_text_0)
    client.chat_postMessage(channel=cloudreach_client_records, text="- 2nd Coordinate : "+user_text_1)
    client.chat_postMessage(channel=cloudreach_client_records, text="- 3rd Coordinate : "+user_text_2)
    client.chat_postMessage(channel=cloudreach_client_records, text="--------------------------------")
    
    c1 = user_text_0.split(" ")
    c2 = user_text_1.split(" ")
    c3 = user_text_2.split(" ")
    
    
    table.put_item(Item= {'id': '1', 'codin10': str(c1[0]), 'codin11': str(c1[1]) , 'codin20' : str(c2[0]), 'codin21': str(c2[1]), 'codin30': str(c3[0]), 'codin31': str(c3[1]) })
    
    print("Your Pirate ships are deployed in positioning [S] marks on the metrix: \n")
    BB = np.array([  [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'], 
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'] ])
    BB[int(c1[0])][int(c1[1])] = ':ship:'
    BB[int(c2[0])][int(c2[1])] = ':ship:'
    BB[int(c3[0])][int(c3[1])] = ':ship:'
    print(BB)
    print("------------------------")
    print("Ready for battle now, Play captain to guess coordinates! \n")
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "Matrix Map"},
            
            "blocks": [
                {
                    "type": "section",
                    "text": { "type": "mrkdwn", "text": BB[0][0]+" "+BB[0][1]+" "+BB[0][2]+" "+BB[0][3]+" "+BB[0][4]+ "\n" +  BB[1][0]+" "+BB[1][1]+" "+BB[1][2]+" "+BB[1][3]+" "+BB[1][4]+ "\n" +BB[2][0]+" "+BB[2][1]+" "+BB[2][2]+" "+BB[2][3]+" "+BB[2][4]+ "\n"+BB[3][0]+" "+BB[3][1]+" "+BB[3][2]+" "+BB[3][3]+" "+BB[3][4]+ "\n"+ BB[4][0]+" "+BB[4][1]+" "+BB[4][2]+" "+BB[4][3]+" "+BB[4][4]+ "\n" },
                    
                },
                
            ]
            })

    say(
        blocks=[
                {
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "View Metrix Map"
				},
				"accessory": {
					"type": "button",
					"action_id": "view",
					"text": {
						"type": "plain_text",
						# "emoji": true,
						"text": "View"
					},
					"value": "click_me_123"
				}
			},
                {
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "Click for Continue"
				},
				"accessory": {
					"type": "button",
					"action_id": "continue",
					"text": {
						"type": "plain_text",
						# "emoji": true,
						"text": "Continue"
					},
					"value": "click_me_123"
				}
			},
            {
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "Click for Cancel"
				},
				"accessory": {
					"type": "button",
					"action_id": "cancel",
					"text": {
						"type": "plain_text",
						# "emoji": true,
						"text": "Cancel"
					},
					"value": "click_me_123"
				}
			}
        ],channel="C036HNB7LB1"
    )

@app.action("continue")
def action_button_click(ack, say ):
    ack()
    say(":anchor: *Ships were deployed* \n Ask your colleague to play Captian and guess the coordinates")
    
   

@app.action("cancel")
def action_button_click(ack, say ):
    ack()    
    say(":exclamation: *Clear Data* \n Type 'play' to restart")

@app.action("view")
def action_button_click(ack, body, client, logger, say):
    ack()
    response = table.get_item(Key={'id': '1' })
    c10 = int(response['Item']['codin10'])
    c11 = int(response['Item']['codin11'])
    c20 = int(response['Item']['codin20'])
    c21 = int(response['Item']['codin21'])
    c30 = int(response['Item']['codin30'])
    c31 = int(response['Item']['codin31'])
    BB = np.array([  [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'], 
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'] ])
    BB[int(c10)][int(c11)] = ':ship:'
    BB[int(c20)][int(c21)] = ':ship:'
    BB[int(c30)][int(c31)] = ':ship:'
    print(BB)
    print("------------------------")
    print("Ready for battle now, Play captain to guess coordinates! \n")
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "Matrix Map"},
            
            "blocks": [
                {
                    "type": "section",
                    "text": { "type": "mrkdwn", "text": BB[0][0]+" "+BB[0][1]+" "+BB[0][2]+" "+BB[0][3]+" "+BB[0][4]+ "\n" +  BB[1][0]+" "+BB[1][1]+" "+BB[1][2]+" "+BB[1][3]+" "+BB[1][4]+ "\n" +BB[2][0]+" "+BB[2][1]+" "+BB[2][2]+" "+BB[2][3]+" "+BB[2][4]+ "\n"+BB[3][0]+" "+BB[3][1]+" "+BB[3][2]+" "+BB[3][3]+" "+BB[3][4]+ "\n"+ BB[4][0]+" "+BB[4][1]+" "+BB[4][2]+" "+BB[4][3]+" "+BB[4][4]+ "\n" },
                    
                },
                
            ]
            })
            




# --------------------------------------------------- Captain ----------------------------------------------------------------------------------------
@app.message("captain")
def message_hello(message, say):
    say(
		blocks = [
			{
				"type": "divider"
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*<fakeLink.toUserProfiles.com| Welcome to the game, Let's battle :>*"
				}
			},
			{
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": ":cop: *Captain* \n Guess the coordinates of pirate ship's and destroy them\n"
				},
				"accessory": {
					"type": "button",
					"action_id": "captain",
					"text": {
						"type": "plain_text",
						# "emoji": true,
						"text": "Play"
					},
					"value": "click_me_123"
				}
			}
			
		]
	)

@app.action("captain")
def handle_command(body, ack, client, logger):
    logger.info(body)
    ack()

    res = client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "gratitude-modal-captain",
            "title": {"type": "plain_text", "text": "BattleShip Matrix"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "close": {"type": "plain_text", "text": "Cancel"},
            "blocks": [
                {
                    "type": "input",
                    "block_id": "my_block_0",
                    "element": {"type": "plain_text_input", "action_id": "c1", "placeholder": {"type":  "plain_text","text": "Coordinate digts must be between 0-4 eg. 3 2"}},
                    "label": {"type": "plain_text", "text": "1st Coordinate"},
                },
                {
                    "type": "input",
                    "block_id": "my_block_1",
                    "element": {"type": "plain_text_input", "action_id": "c2", "placeholder": {"type":  "plain_text","text": "Coordinate digts must be between 0-4 eg. 3 2"}},
                    "label": {"type": "plain_text", "text": "2nd Coordinate"},
                },
                {
                    "type": "input",
                    "block_id": "my_block_2",
                    "element": {"type": "plain_text_input", "action_id": "c3", "placeholder": {"type":  "plain_text","text": "Coordinate digts must be between 0-4 eg. 3 2"}},
                    "label": {"type": "plain_text", "text": "3rd Coordinate"},
                }
                ]
        }
    )
    logger.info(res)

@app.view("gratitude-modal-captain")
def view_submission(ack, body, client, logger, say):
    ack()

    # # NumPy array
    # A = np.array([  [1, 2, 3, 4, 5], 
    #                 [6, 7, 8, 9, 10],
    #                 [11, 12, 13, 14, 15],
    #                 [16, 17, 18, 19, 20],
    #                 [21, 22, 23, 24, 25] ])
    # input captain coordinates
    logger.info(body["view"]["state"]["values"])
    # Extra Credit: Uncomment out this section
    cloudreach_client_records = "C036HNB7LB1"
    user_text_0 = body["view"]["state"]["values"]["my_block_0"]["c1"]["value"]
    user_text_1 = body["view"]["state"]["values"]["my_block_1"]["c2"]["value"]
    user_text_2 = body["view"]["state"]["values"]["my_block_2"]["c3"]["value"]
    
    client.chat_postMessage(channel=cloudreach_client_records, text=":pushpin: Your Coordinates :")
    client.chat_postMessage(channel=cloudreach_client_records, text="- 1st Coordinate : "+user_text_0)
    client.chat_postMessage(channel=cloudreach_client_records, text="- 2nd Coordinate : "+user_text_1)
    client.chat_postMessage(channel=cloudreach_client_records, text="- 3rd Coordinate : "+user_text_2)
    client.chat_postMessage(channel=cloudreach_client_records, text="--------------------------------")
    
    c1 = user_text_0.split(" ")
    c2 = user_text_1.split(" ")
    c3 = user_text_2.split(" ")
    # Write:
    table.put_item(Item= {'id': '2', 'codin10': str(c1[0]), 'codin11': str(c1[1]) , 'codin20' : str(c2[0]), 'codin21': str(c2[1]), 'codin30': str(c3[0]), 'codin31': str(c3[1]) })
    # # captain coordinates
    # c10 = c1[0]
    # c11 = c1[1]
    # c20 = c2[0]
    # c21 = c2[1]
    # c30 = c3[0]
    # c31 = c3[1]
    # CaptianCoordinate1 = A[int(c10)][int(c11)]
    # CaptianCoordinate2 = A[int(c20)][int(c21)]
    # CaptianCoordinate3 = A[int(c30)][int(c31)]
    # CaptianCoordinateList = [CaptianCoordinate1, CaptianCoordinate2, CaptianCoordinate3]
    
    

    BB = np.array([  [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'], 
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'] ])
    BB[int(c1[0])][int(c1[1])] = ':pushpin:'
    BB[int(c2[0])][int(c2[1])] = ':pushpin:'
    BB[int(c3[0])][int(c3[1])] = ':pushpin:'
    print(BB)
    print("------------------------")
    print("Ready for battle now, Play captain to guess coordinates! \n")
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "Matrix Map"},
            
            "blocks": [
                {
                    "type": "section",
                    "text": { "type": "mrkdwn", "text": BB[0][0]+" "+BB[0][1]+" "+BB[0][2]+" "+BB[0][3]+" "+BB[0][4]+ "\n" +  BB[1][0]+" "+BB[1][1]+" "+BB[1][2]+" "+BB[1][3]+" "+BB[1][4]+ "\n" +BB[2][0]+" "+BB[2][1]+" "+BB[2][2]+" "+BB[2][3]+" "+BB[2][4]+ "\n"+BB[3][0]+" "+BB[3][1]+" "+BB[3][2]+" "+BB[3][3]+" "+BB[3][4]+ "\n"+ BB[4][0]+" "+BB[4][1]+" "+BB[4][2]+" "+BB[4][3]+" "+BB[4][4]+ "\n" },
                    
                },
                
            ]
            })

    say(
        blocks=[
                {
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "View Metrix Map"
				},
				"accessory": {
					"type": "button",
					"action_id": "cview",
					"text": {
						"type": "plain_text",
						# "emoji": true,
						"text": "View"
					},
					"value": "click_me_123"
				}
			},
                {
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "Click for Continue"
				},
				"accessory": {
					"type": "button",
					"action_id": "ccontinue",
					"text": {
						"type": "plain_text",
						# "emoji": true,
						"text": "Continue"
					},
					"value": "click_me_123"
				}
			},
            {
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "Click for Cancel"
				},
				"accessory": {
					"type": "button",
					"action_id": "ccancel",
					"text": {
						"type": "plain_text",
						# "emoji": true,
						"text": "Cancel"
					},
					"value": "click_me_123"
				}
			}
        ],channel="C036HNB7LB1"
    )

@app.action("ccontinue")
def action_button_click(ack, say ):
    ack()
    # NumPy array
    A = np.array([  [1, 2, 3, 4, 5], 
                    [6, 7, 8, 9, 10],
                    [11, 12, 13, 14, 15],
                    [16, 17, 18, 19, 20],
                    [21, 22, 23, 24, 25] ])
    # get the pirates coordinates  
    # Get item
    response = table.get_item(Key={'id': '1' })
    p_coordinates10 = int(response['Item']['codin10'])
    p_coordinates11 = int(response['Item']['codin11'])
    p_coordinates20 = int(response['Item']['codin20'])
    p_coordinates21 = int(response['Item']['codin21'])
    p_coordinates30 = int(response['Item']['codin30'])
    p_coordinates31 = int(response['Item']['codin31'])

    PshipCordinate1 = A[p_coordinates10][p_coordinates11]
    PshipCordinate2 = A[p_coordinates20][p_coordinates21]
    PshipCordinate3 = A[p_coordinates30][p_coordinates31]
    PShipCoordinateList = [PshipCordinate1, PshipCordinate2, PshipCordinate3]

    # captain coordinates
    response = table.get_item(Key={'id': '2' })
    c10 = int(response['Item']['codin10'])
    c11 = int(response['Item']['codin11'])
    c20 = int(response['Item']['codin20'])
    c21 = int(response['Item']['codin21'])
    c30 = int(response['Item']['codin30'])
    c31 = int(response['Item']['codin31'])
    CaptianCoordinate1 = A[int(c10)][int(c11)]
    CaptianCoordinate2 = A[int(c20)][int(c21)]
    CaptianCoordinate3 = A[int(c30)][int(c31)]
    CaptianCoordinateList = [CaptianCoordinate1, CaptianCoordinate2, CaptianCoordinate3]

    
    DestroyList = set(CaptianCoordinateList) & set(PShipCoordinateList)
        # print(TargetAreaList)
    if len(DestroyList):
            print("BOOOOM! WELLDONE, YOU HAVE DISTROYED "+str(len(DestroyList))+" PIRATE SHIPs")
            say(":boom: *Well done!* You have destroyed [" +str(len(DestroyList))+ "] pirate ships")
 
    else:
            missed = 3 - int(len(DestroyList))
            print("YOU MISSED ["+ str(missed) + "] pirate ships, RECALCULATE YOUR COORDINATES AND TRY AGAIN!")
            say(":unamused: *YOU MISSED* ["+ str(missed) + "] pirate ships, RECALCULATE YOUR COORDINATES AND TRY AGAIN!")
    
   

@app.action("ccancel")
def action_button_click(ack, say ):
    ack()    
    say(":exclamation: *Clear Data* \n Type 'play' to restart")

@app.action("cview")
def action_button_click(ack, body, client, logger, say):
    ack()
    response = table.get_item(Key={'id': '2' })
    c10 = int(response['Item']['codin10'])
    c11 = int(response['Item']['codin11'])
    c20 = int(response['Item']['codin20'])
    c21 = int(response['Item']['codin21'])
    c30 = int(response['Item']['codin30'])
    c31 = int(response['Item']['codin31'])
    BB = np.array([  [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'], 
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'],
                    [':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:', ':white_circle:'] ])
    BB[int(c10)][int(c11)] = ':rocket:'
    BB[int(c20)][int(c21)] = ':rocket:'
    BB[int(c30)][int(c31)] = ':rocket:'
    print(BB)
    print("------------------------")
    print("Ready for battle now, Play captain to guess coordinates! \n")
    ack()
    # Call views_open with the built-in client
    client.views_open(
        # Pass a valid trigger_id within 3 seconds of receiving it
        trigger_id=body["trigger_id"],
        # View payload
        view={
            "type": "modal",
            # View identifier
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text": "Matrix Map"},
            
            "blocks": [
                {
                    "type": "section",
                    "text": { "type": "mrkdwn", "text": BB[0][0]+" "+BB[0][1]+" "+BB[0][2]+" "+BB[0][3]+" "+BB[0][4]+ "\n" +  BB[1][0]+" "+BB[1][1]+" "+BB[1][2]+" "+BB[1][3]+" "+BB[1][4]+ "\n" +BB[2][0]+" "+BB[2][1]+" "+BB[2][2]+" "+BB[2][3]+" "+BB[2][4]+ "\n"+BB[3][0]+" "+BB[3][1]+" "+BB[3][2]+" "+BB[3][3]+" "+BB[3][4]+ "\n"+ BB[4][0]+" "+BB[4][1]+" "+BB[4][2]+" "+BB[4][3]+" "+BB[4][4]+ "\n" },
                    
                },
                
            ]
            })
            























# @app.action("pirate")
# def action_button_click(body, ack, say):
#     # Acknowledge the action
#     ack()
#     say(f"Welcome to the battle field pirate <@{body['user']['id']}>. Lets start deploying the ships")
#     open_modal(ack, body, client)





# @app.action("captain")
# def action_button_click(body, ack, say):
#     # Acknowledge the action
#     ack()
#     say(f"Welcome to the battle field captain <@{body['user']['id']}>. Start guessing cordinates of deployed pirate ships! ")




# def open_modal(ack, body, client):
#     # Acknowledge the command request
#     ack()
#     # Call views_open with the built-in client
#     client.views_open(
#         # Pass a valid trigger_id within 3 seconds of receiving it
#         trigger_id=body["trigger_id"],
#         # View payload
#         view={
#             "type": "modal",
#             # View identifier
#             "callback_id": "view_1",
#             "title": {"type": "plain_text", "text": "My App"},
#             "submit": {"type": "plain_text", "text": "Submit"},
#             "blocks": [
#                 {
#                     "type": "section",
#                     "text": {"type": "mrkdwn", "text": "Welcome to a modal with _blocks_"},
#                     "accessory": {
#                         "type": "button",
#                         "text": {"type": "plain_text", "text": "Click me!"},
#                         "action_id": "button_abc"
#                     }
#                 },
#                 {
#                     "type": "input",
#                     "block_id": "input_c",
#                     "label": {"type": "plain_text", "text": "What are your hopes and dreams?"},
#                     "element": {
#                         "type": "plain_text_input",
#                         "action_id": "dreamy_input",
#                         "multiline": True
#                     }
#                 }
#             ]
#         }
#     )



# @app.command("/com")
# def repeat_text(ack, respond, command):
#     # Acknowledge command request
#     ack()
#     respond(f"{command['text']}")
















# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
