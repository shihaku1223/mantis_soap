#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

from mantisconnect.connector import MantisSoapConnector
from mantisconnect.project import Issue

class IssueViewer:
    def __init__(self, issue):
        self._issue = issue

    def getNotes(self):
        if len(self._issue['notes']) == 0:
            return None

        return issue['notes']

    def getAttachments(self):
        if len(self._issue['attachments']) == 0:
            return None

        return self._issue['attachments']

    # return datetime.datetime object
    def getLastUpdatedTime(self):
        return self._issue['last_updated']
