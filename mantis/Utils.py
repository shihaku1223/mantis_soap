#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from mantis.Connector import Connector

def updateIssueStatus(connector, issueId, statusId):

    issue = connector.getIssue(issueId)

    print_flush(connector.updateIssueStatus(issue, statusId))

def addNote(connector, issueId, reporter, message):

    return connector.addNote(issueId, reporter, message)

def changeIssueProject(connector, issueId, projectId):
    issue = connector.getIssue(issueId)
    users = connector.getProjectUsers(projectId)

    return connector.updateIssueProjectId(issue, projectId)
