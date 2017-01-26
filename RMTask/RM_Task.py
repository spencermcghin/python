"""Slack slash command for jira interaction."""
from flask import Flask
from flask_slack import Slack
from slackclient import SlackClient
from jira import JIRA
from jira.exceptions import JIRAError
import json
import os


JIRA_URL = os.getenv('JIRA_URL')
options = {
    'server': JIRA_URL,
}
jira = JIRA(
    options,
    basic_auth=(
        os.getenv('JIRA_USER'),
        os.getenv('JIRA_PASSWORD')))

app = Flask(__name__)
slack = Slack(app)
sc = SlackClient(os.getenv('SLACK_TOKEN'))
app.add_url_rule('/', view_func=slack.dispatch)


"""Entry point for /jiratask. """


@slack.command(
    'jiratask',
    token=os.getenv('SLACK_SLASH_TOKEN'),
    team_id=os.getenv('SLACK_TEAM_ID'),
    methods=['POST'])
def __jira_handle(**kwargs):
    user = get_jira_username_from_slack(kwargs.get('user_id'))
    channel = kwargs.get('channel_id')
    command = kwargs.get('text').partition(' ')[0].lower()
    jira_key = kwargs.get('text').partition(' ')[2].partition(' ')[0].upper()
    jira_data = kwargs.get('text').partition(' ')[2].partition(' ')[2]


def get_jira_username_from_slack(user_id):
    response = json.loads(sc.api_call('users.info', user=user_id))
    if response.get("ok"):
        slack_user = response['user']['profile']['email']
        return get_jira_username(slack_user)
    return ""


def get_jira_username(user_id):
    user = jira.search_users(user_id)
    return user[0].name if len(user) == 1 else ''


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)



