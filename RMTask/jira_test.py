# Imports
from jira import JIRA

user = 'spencer.mcghin@rittmanmead.com'
password = ''
server = 'https://rittmanmead.atlassian.net'
options = {'server': server}
jira = JIRA(options=options, basic_auth=(user, password))


def connect_jira(jira_server, jira_user, jira_password):
    # Connect to JIRA. Return None on error
    try:
        print('Connecting to JIRA server at: {}'.format(server))
    except Exception as e:
        print("Failed to connect to JIRA: %s" % e)
        return None


def jira_issue():
    try:
        issue_dict = {
            "project": {"key": 'SM'},
            "summary": "something's wrong",
            "description": "test",
            "issuetype": {"name": "Task"}
        }
        new_issue = jira.create_issue(fields=issue_dict)
        return new_issue
    except Exception as e:
        print(e)
        return None


connect_jira(jira_server=server, jira_user=user, jira_password=password)
jira_issue()
