#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import base64
import magic
from pathlib import Path

from mantis.Connector import Connector

def updateIssueStatus(connector, issueId, statusId):

    issue = connector.getIssue(issueId)

    return connector.updateIssueStatus(issue, statusId)

def addNote(connector, issueId, name, message):

    accountType = connector._mc.client.get_type('ns0:AccountData')
    accountData = accountType(name = name)

    return connector.addNote(issueId, accountData, message)

def changeIssueProject(connector, issueId, projectId):
    issue = connector.getIssue(issueId)
    users = connector.getProjectUsers(projectId)

    return connector.updateIssueProjectId(issue, projectId)

def addAttachment(connector, issueId, filePath):

    p = Path(filePath)
    mime = magic.Magic(mime=True)
    mimeType = mime.from_file(filePath)

    base64String = None
    with open(filePath, 'rb') as file:
        base64String = base64.b64encode(file.read())

    return connector.addAttachment(issueId, p.name, mimeType, base64String)

def downloadAttachment(connector, attachmentId, destPath):
    byteArray = connector.getIssueAttachment(attachmentId)
    with open(destPath, 'wb') as f:
        f.write(byteArray)
