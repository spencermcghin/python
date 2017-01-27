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


"""Entry point for /jiratask."""


@slack.command(
    'jiratask',
    token=os.getenv('SLACK_SLASH_TOKEN'),
    team_id=os.getenv('SLACK_TEAM_ID'),
    methods=['POST'])
def __jira_handle(**kwargs):
    user = __get_jira_username_from_slack(kwargs.get('user_id'))
    channel = kwargs.get('channel_id')
    jira_key = kwargs.get('text').partition(' ')[2].partition(' ')[0].upper()
    jira_data = kwargs.get('text').partition(' ')[2].partition(' ')[2]


def __get_jira_username_from_slack(user_id):
    response = json.loads(sc.api_call('users.info', user=user_id))
    if response.get("ok"):
        slack_user = response['user']['profile']['email']
        return __get_jira_username(slack_user)
    return ""


def __get_jira_username(user_id):
    user = jira.search_users(user_id)
    return user[0].name if len(user) == 1 else ''


def __jira_validate_projectkey(key):
    projects = jira.projects()
    for proj in projects:
        if proj.key == key:
            return True
    return False


def __jira_validate_issue(key):
    try:
        jira.issue(key)
        return True
    except JIRAError:
        return False


# Create and send issue
def __send_message_issue(issue, channel):
    attach = [{
         'text': '*' + issue.fields.summary + '*\n\n *Assignee* ' +
              issue.fields.assignee.name + ' *Priority* ' +
              issue.fields.priority.name,
              'title': issue.key,
              'title_link': JIRA_URL + "/browse/" + issue.key,
              'mrkdwn_in': ['text',
                            'pretext']
              }]
    send_data = {
           'channel': channel,
           'username': 'Jira Bot',
           'attachments': json.dumps(attach),
           'mrkdwn': True,
           'as_user': False}
    msg = json.loads(sc.api_call('chat.postMessage', **send_data))
    return msg


def __jira_create_task(user, channel, project, summary):
    return __jira_create(user, channel, project, summary, 'Task')


def __jira_create(user, channel, project, summary, issuetype):

    issue_dict = {
                'project': {'key': project},
                'summary': summary,
                'reporter': {'name': user},
                'issuetype': {'name': issuetype},
                'assignee': {'name': user},
            }
    new_issue = jira.create_issue(fields=issue_dict)
    return __send_message_issue(new_issue, channel)


if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)



