#!/usr/bin/env python3
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

    def getIssueAttachment(self, id):
        attachment = self._mc.client.service.mc_issue_attachment_get(
            self._mc.user_name,
            self._mc.user_passwd,
            id)
        return attachment

    def getProjectIssues(self, projectId, page = 0, itemPerPage = 50):
        mc = self._mc

        issues = self._mc.client.service.mc_project_get_issues(
            mc.user_name,
            mc.user_passwd,
            projectId, page, itemPerPage)

        return issues

    def getProjectUsers(self, projectId):
        mc = self._mc

        users = self._mc.client.service.mc_project_get_users(
            mc.user_name,
            mc.user_passwd,
            projectId, 0)
        return users

    def addNote(self, issueId, accountData, message):
        mc = self._mc

        noteType = self._mc.client.get_type('ns0:IssueNoteData')
        note = noteType(reporter = accountData, text = message)

        response = self._mc.client.service.mc_issue_note_add(
            mc.user_name,
            mc.user_passwd,
            issueId,
            note)

        return response

    def updateIssueStatus(self, originIssue, accountData, statusId):
        mc = self._mc

        objType = self._mc.client.get_type('ns0:ObjectRef')

        status = objType(id = statusId)
        project = objType(id = originIssue['project']['id'])
        category = originIssue['category']

        issueType = self._mc.client.get_type('ns0:IssueData')
        issue = issueType(
            project = project,
            category = category,
            summary = originIssue['summary'],
            description = originIssue['description'],
            reporter = accountData, status = status)

        response = self._mc.client.service.mc_issue_update(
            mc.user_name,
            mc.user_passwd,
            originIssue['id'],
            issue)

        return response

    def updateIssueProjectId(self, originIssue, projectId):
        mc = self._mc

        objType = mc.client.get_type('ns0:ObjectRef')
        project = objType(id = projectId)
        category = originIssue['category']
        reporter = originIssue['reporter']

        issueType = self._mc.client.get_type('ns0:IssueData')
        issue = issueType(
            project = project,
            category = category,
            summary = originIssue['summary'],
            description = originIssue['description'],
            reporter = reporter)

        response = mc.client.service.mc_issue_update(
            mc.user_name,
            mc.user_passwd,
            originIssue['id'],
            issue)

        return response
