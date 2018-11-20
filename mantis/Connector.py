#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

from mantisconnect.connector import MantisSoapConnector
from mantisconnect.project import Issue

class Connector:
    def __init__(self, url, username, password):
        self._mc = MantisSoapConnector(url)
        self._mc.set_user_passwd(username, password)

    def connect(self):
        self._mc.connect()

    def getVersion(self):
        return self._mc.version

    def getIssue(self, id):
        issue = self._mc.request_issue_get(id)
        return issue

    def getProjectId(self, name):
        project = self._mc.request_project(name)

        if project == 0:
            return None
        return project

    def getProjectIssues(self, projectId, page = 0, itemPerPage = 50):
        mc = self._mc

        issues = self._mc.client.service.mc_project_get_issues(
            mc.user_name,
            mc.user_passwd,
            projectId, page, itemPerPage)

        return issues
