#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from mantisconnect.connector import MantisSoapConnector
from mantisconnect.project import Issue

class IssueViewer:
    def __init__(self, issue):
        self._issue = issue

    def getId(self):
        return self._issue['id']

    def getNotes(self):
        if len(self._issue['notes']) == 0:
            return None

        return self._issue['notes']

    def getViewStateName(self):
        return self._issue['view_state']['name']

    def getStatusName(self):
        return self._issue['status']['name']

    def getCategory(self):
        return self._issue['category']

    def getAttachments(self):
        if len(self._issue['attachments']) == 0:
            return None

        return self._issue['attachments']

    def getSubmittedDate(self):
        return self._issue['date_submitted']

    def getProjectId(self):
        return self._issue['project']['id']

    def getProjectName(self):
        return self._issue['project']['name']

    def getReporter(self):
        return self._issue['reporter']

    def getReporterRealName(self):
        return self._issue['reporter']['real_name']

    def getReporterName(self):
        return self._issue['reporter']['name']

    def getReporterEmail(self):
        return self._issue['reporter']['email']

    def getDescription(self):
        return self._issue['description']

    # return datetime.datetime object
    def getLastUpdatedTime(self):
        return self._issue['last_updated']
