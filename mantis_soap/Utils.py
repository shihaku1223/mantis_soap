#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import base64
import mimetypes
from pathlib import Path

from mantis_soap.Connector import Connector

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
    mimeType = mimetypes.guess_type(filePath)[0]

    base64String = None
    with open(filePath, 'rb') as f:
        binary = f.read()
        base64String = base64.b64encode(binary).decode()

    return connector.addAttachment(issueId, p.name, mimeType, base64String)

def downloadAttachment(connector, attachmentId, destPath):
    byteArray = connector.getIssueAttachment(attachmentId)
    with open(destPath, 'wb') as f:
        f.write(byteArray)
