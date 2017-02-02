# The parameters included in a slash command request (with example values):
#   token=gIkuvaNzQIHg97ATvDxqgjt
#   team_id=T0001
#   team_domain=example
#   channel_id=C2147483705
#   channel_name=test
#   user_id=U2147483697
#   user_name=Steve
#   command=/weather
#   text=94070
#   response_url=https://hooks.slack.com/commands/1234/5678


# Imports
from flask import *
from slackclient import SlackClient
from jira import JIRA



# Slack Variables
slack_client = SlackClient('xoxp-2510066817-2543864854-133850972935-d17f532401c086cd5a98d05ef71a8775')
slack_user = request.form.get('user_name', None)
slack_token = request.form.get('token', None)
slack_text = request.form.get('text', None)

# JIRA Variables
jira_user = 'spencer.mcghin'
password = 'BLADErunner1'
server = 'https://rittmanmead.atlassian.net'
options = {'server': server}
jira = JIRA(options=options, basic_auth=(jira_user, password))
jira_project = slack_text.split(' ')[0]
jira_description = slack_text.split(' ')[1:]

# Flask Variables
app = Flask(__name__)


# Functions for Program

# Establish connection to RM JIRA server
def connect_jira(jira_server, jira_user, jira_password):
    # Connect to JIRA. Return None on error
    try:
        print('Connecting to JIRA server at: {}'.format(server))
        return jira
    except Exception as e:
        print("Failed to connect to JIRA: %s" % e)
        return None


# Create Task Issue on
def jira_issue(project, description):
        try:
            issue_dict = {
                "project": {"key": project},
                "summary": description,
                "issuetype": {"name": "Task"},
                "assignee": ''
            }
            new_issue = jira.create_issue(fields=issue_dict)
            return new_issue
        except Exception as e:
            print(e)
            return None


# def jira_project_list():
#     try:


# Function to get args from slack
@app.route("/jiratask", methods=['POST'])
def slack_response():
    token = request.form.get('token', None)
    text = request.form.get('text', None)
    if not token:
        abort(400)

    return jsonify({
        'response_type': 'in_channel',
        'text': '{}'.format(text.split(' ')[0]),
        'attachments': [
            {
                'fallback': 'Required plain-text summary of the attachment.',
                'color': '#36a64f',
                'author_name': jira_user,
                'author_icon': 'https://www.atlassian.com/docroot/wac/resources/wac/img/social-icons/jira_logo.jpg',
                'title': 'JIRA Task Created - {0}'.format(text.split(' ')[1:]),
                'title_link': 'https://rittmanmead.atlassian.net',
                'image_url': 'https://www.rittmanmead.com/blog/content/images/2017/02/doge1.jpg',
                'thumb_url': 'https://www.rittmanmead.com/blog/content/images/2017/02/doge1.jpg'
            }
        ]
    })


if __name__ == '__main__':
    connect_jira(jira_server=server, jira_user=jira_user, jira_password=password)
    if slack_text:
        try:
            create_issue = jira_issue(jira_project, jira_description)
        except Exception as e:
            print(e)
    app.run(debug=True, host='localhost', port=5000)



