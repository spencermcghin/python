""" Create an rmtask slash command for slack integration with JIRA. """

# Imports
from flask import Flask
from flask_slack import Slack
from slackclient import SlackClient
from jira import JIRA
from jira.exceptions import JIRAError
import json
import os


# Variables
SLACK_TOKEN = os.environ.get('SLACK_TOKEN')
slack_client = SlackClient(SLACK_TOKEN)
