<h1>WELCOME TO Guess & Destroy SLACK APP</h1>

1. Create DynamoDB table "**Coordinates**" and partition key "**id**"
2. Run **main.py**

refernce : https://slack.dev/bolt-python/tutorial/getting-started
Instruction :
```
    
        1. mkdir first-bolt-app
        2. cd first-bolt-app
        3. python3 -m venv .venv
        4. source .venv/bin/activate    to confirm : < which python3 >
                4.1     python -m pip install boto3
                4.2.    pip install numpy

        5. Navigate to the OAuth & Permissions on the left sidebar and scroll down to the Bot Token Scopes section. Click Add an OAuth Scope.
        6. For now, we’ll just add one scope: chat:write. This grants your app the permission to post messages in channels it’s a member of.
        7. Scroll up to the top of the OAuth & Permissions page and click Install App to Workspace. You’ll be led through Slack’s OAuth UI, where you should allow your app to be installed to your development workspace.
        8. Once you authorize the installation, you’ll land on the OAuth & Permissions page and see a Bot User OAuth Access Token.
        9. Copy your app-level (xapp) token from the Basic Information page and then store it in a new environment variable.-export SLACK_APP_TOKEN=<your-app-level-token>

        10. Then head over to Basic Information and scroll down under the App Token section and click Generate Token and Scopes to generate an app-level token. Add the connections:write scope to this token and save the generated xapp token, we’ll use both these tokens in just a moment.
        11. Copy your bot (xoxb) token from the OAuth & Permissions page and then store it in a new environment variable.- export SLACK_BOT_TOKEN=xoxb-<your-bot-token>
        12. Navigate to Socket Mode on the left side menu and toggle to enable.

        13. pip install slack_bolt
        14. Create a new file called app.py in this directory and add the following code:
        15. run your env file

        16. Navigate to Event Subscriptions on the left sidebar and toggle to enable. Under Subscribe to Bot Events, you can add events for your bot to respond to. There are four events related to messages:

                message.channels listens for messages in public channels that your app is added to
                message.groups listens for messages in 🔒 private channels that your app is added to
                message.im listens for messages in your app’s DMs with users
                message.mpim listens for messages in multi-person DMs that your app is added to




        16. python3 app.py - should run bolt app!

        17. 
```
Thank you!
PK Pasyala