
# Imports
from flask import *
from slackclient import SlackClient
import urllib
import json
# from jira import JIRA


# JIRA Variables
# jira = JIRA()
key = ''
username = 'spencer.mcghin@rittmanmead.com'
password = ''
# jira_auth = JIRA(basic_auth=(username, password))
# jira_url = JIRA('https://rittmanmead.atlassian.net')

# Slack Variables
slack_client = SlackClient('xoxp-2510066817-2543864854-133850972935-d17f532401c086cd5a98d05ef71a8775')


# The parameters included in a slash command request (with example values):
#   token=gIkuvaNzQIHg97ATvDxqgjtO
#   team_id=T0001
#   team_domain=example
#   channel_id=C2147483705
#   channel_name=test
#   user_id=U2147483697
#   user_name=Steve
#   command=/weather
#   text=94070
#   response_url=https://hooks.slack.com/commands/1234/5678

# Flask Variables
app = Flask(__name__)

# Functions for Program


# Function to get args from slack
@app.route("/jiratask", methods=['POST'])
def slack_response():
    token = request.form.get('token', None)
    text = request.form.get('text', None)
    project = text.split(' ')[0]
    description = text.split(' ')[1]
    user_name = request.form.get('user_name', None)

    if not token:
        abort(400)

    return jsonify({
        # Uncomment the line below for the response to be visible to everyone
        'response_type': 'in_channel',
        'text': project,
        'attachments': [
            {
                'fallback': 'Required plain-text summary of the attachment.',
                'color': '#36a64f',
                'author_name': user_name,
                'author_icon': 'https://www.atlassian.com/docroot/wac/resources/wac/img/social-icons/jira_logo.jpg',
                'title': 'JIRA Task Created - {0}'.format(description),
                'title_link': 'https://rittmanmead.atlassian.net',
                'image_url': 'https://www.rittmanmead.com/blog/content/images/2017/02/doge1.jpg',
                'thumb_url': 'https://www.rittmanmead.com/blog/content/images/2017/02/doge1.jpg'
            }
        ]
    })

# TODO - Create get user project list command out of JIRA


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)



