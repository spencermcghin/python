""" Create an rmtask slash command for slack integration with JIRA. """

# Imports
from flask import Flask
from flask_slack import Slack
from slackclient import SlackClient
from jira import JIRA
from jira.exceptions import JIRAError
import json
import os


# Slack Variables
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
slack_client = SlackClient(SLACK_TOKEN)


# Jira Variables
jira_uri = 'https://rittmanmead.atlassian.net/'


# Flask
app = Flask(__name__)


@app.route('/hello', methods=['POST'])
def hello():
    return 'Hello Slack!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)