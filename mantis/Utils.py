#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from mantis.Connector import Connector

def updateIssueStatus(connector, issueId, statusId):

    issue = connector.getIssue(issueId)

    print_flush(connector.updateIssueStatus(issue, statusId))

def addNote(connector, issueId, message):

    projectId = connector.getProjectId(options.project)
    users = connector.getProjectUsers(projectId)
    """
    accountType = self._mc.client.get_type('ns0:AccountData')
    accountData = accountType(id = 909, name = '10079186', real_name = '王\u3000詩博', email = 'sibo_wang@ot.olympus.co.jp')
    """
    reporter = None
    for user in users:
        if user['name'] == options.username:
            reporter = user

    print_flush('New note add {}\n'.format(
        connector.addNote(issueId, reporter, message)))

def changeIssueProject(connector, issueId, projectId):
    issue = connector.getIssue(issueId)
    users = connector.getProjectUsers(projectId)

    return connector.updateIssueProjectId(issue, projectId)
